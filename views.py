from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return "<html>" \
           "<head>" \
           "<title> " \
           "</title>" \
           "<center " \
           "</head> " \
           "<body> " \
           "<h1>Microeconomics Calculator</h1>" \
           "<h2><i>By Olivier Meyer</i></h2>" \
           "<p>1</p>" \
           "<p>2</p>" \
           "<p>Select one of the following function forms:</p>" \
           "</center>" \
           "</body>" \
           "</FONT>" \
           "</html>"
