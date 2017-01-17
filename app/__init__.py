from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.debug = False
#app.debug = True

#if (app.debug):
  #from werkzeug.debug import DebuggedApplication
  #app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

from pages.views import pageView as pageView
app.register_blueprint(pageView)
