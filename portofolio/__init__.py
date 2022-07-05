from flask import Flask
from .views import views




app = Flask(__name__)
app.config["SECRET_KEY"] =  "692a2869afdf7757c8e47af294266adb6833839d1ed63afb"

app.register_blueprint(views)