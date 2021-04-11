from flask import Flask, render_template


def init_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dtsproa"
    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app