from flask import Flask
from views import views

app = Flask(__name__, template_folder='templates')
app.register_blueprint(views, url_prefixe="/views")

if __name__ == '__main__':
    app.run(debug=True)
