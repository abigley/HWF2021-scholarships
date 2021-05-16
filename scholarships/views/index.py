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