from flask import Blueprint, render_template

pageView = Blueprint('pageView', __name__, template_folder="templates")

@pageView.route('/', methods=['GET'])
def index():
  newVar = "Hello World" 
  return render_template('pages/index.html', newVar=newVar)
