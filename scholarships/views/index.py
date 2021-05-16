"""
Scholarships index (main) view.
URLs include:
/
"""
import flask
import scholarships
@scholarships.app.route('/')
def show_index():
    """Display / route."""
    flask.session["user_id"] = None
    context = {}
    return flask.render_template("index.html", **context)


@scholarships.app.route('/browse/')
def show_browse():
    """Display browse route."""
    ex_context = {"scholarships": [
        {"title": "Kessler Scholarship",
        "link": "https://lsa.umich.edu/scholarships/irene-and-morris-b-kessler-presidential-scholarship.html",
        "description": "The Kessler Presidential Scholars Program supports a diverse community of first-generation college students at U-M."},
        {"title": "U.P. Scholars",
        "link": "https://lsa.umich.edu/scholarships/UPScholars.html",
        "description": "A new community tailored to support incoming students from Michigan's Upper Peninsula."}
    ]}
    return flask.render_template("browse.html", **ex_context)


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
    context = {"username": user, "scholarships": 
        [
        {"title": "Kessler Scholarship",
        "link": "https://lsa.umich.edu/scholarships/irene-and-morris-b-kessler-presidential-scholarship.html",
        "description": "The Kessler Presidential Scholars Program supports a diverse community of first-generation college students at U-M."},
        {"title": "U.P. Scholars",
        "link": "https://lsa.umich.edu/scholarships/UPScholars.html",
        "description": "A new community tailored to support incoming students from Michigan's Upper Peninsula."}
    ]}
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


