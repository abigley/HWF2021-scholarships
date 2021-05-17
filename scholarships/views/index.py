""" Scholarships app views."""
import flask
import scholarships
from googleapiclient.discovery import build
from google.oauth2 import service_account

@scholarships.app.route('/')
def show_index():
    """Display / route."""
    flask.session["user_id"] = None
    context = {}
    return flask.render_template("index.html", **context)


@scholarships.app.route('/browse/')
def show_browse():
    """Display browse route."""
    scholarship_list = google_sheets_import()
    ex_context = {"scholarships": [
        {"title": "Kessler Scholarship",
        "link": "https://lsa.umich.edu/scholarships/irene-and-morris-b-kessler-presidential-scholarship.html",
        "description": "The Kessler Presidential Scholars Program supports a diverse community of first-generation college students at U-M."},
        {"title": "U.P. Scholars",
        "link": "https://lsa.umich.edu/scholarships/UPScholars.html",
        "description": "A new community tailored to support incoming students from Michigan's Upper Peninsula."}
    ]}
    context = {"scholarships": scholarship_list}
    return flask.render_template("browse.html", **context)


@scholarships.app.route('/accounts/login/')
def show_login():
    """Display login route."""
    context = {}
    return flask.render_template("login.html")

@scholarships.app.route('/u/')
def show_user():
    """Display personalized results."""
    user = flask.session.get("user_id")
    if user is None:
        return flask.redirect(flask.url_for("show_login"))
    scholarship_list = google_sheets_import()
    womens_schols = []
    for scholarship in scholarship_list:
        if "Women" in scholarship["Tags"]:
            womens_schols.append(scholarship)
    ex_context = {"username": user, "scholarships": 
        [
        {"title": "Kessler Scholarship",
        "link": "https://lsa.umich.edu/scholarships/irene-and-morris-b-kessler-presidential-scholarship.html",
        "description": "The Kessler Presidential Scholars Program supports a diverse community of first-generation college students at U-M."},
        {"title": "U.P. Scholars",
        "link": "https://lsa.umich.edu/scholarships/UPScholars.html",
        "description": "A new community tailored to support incoming students from Michigan's Upper Peninsula."}
    ]}
    context = {"username": user, "scholarships": womens_schols}
    return flask.render_template("user.html", **context)


@scholarships.app.route('/accounts/', methods=['POST'])
def login_post():
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    if username is None or password is None:
        return flask.redirect(flask.request.args.get('target'))
    else:
        flask.session["user_id"] = username
        return flask.redirect(flask.url_for("show_user"))


def google_sheets_import():
    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    #SPREADSHEET_ID = '1_knx7erZbVlhx0Y4e7aig1RlrhYHhC8AxjlqDI4_qpA'
    SPREADSHEET_ID = '1UJOY-LAuKcIz-C-C0KpYutzKfXEe4vqB4W1Md0QiZy8'

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range='MS!A1:YY').execute()
    values = result.get('values', [])
    val_list = []
    for i in range(1, len(values)):
        val_dict = {}
        for j, title in enumerate(values[0]):
            if len(values[i]) > j:
                val_dict[title] = values[i][j]
        val_list.append(val_dict)
    print(val_list)
    return val_list