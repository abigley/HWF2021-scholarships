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
    context = {}
    return flask.render_template("browse.html")


@scholarships.app.route('/login/')
def show_login():
    """Display login route."""
    context = {}
    return flask.render_template("login.html")