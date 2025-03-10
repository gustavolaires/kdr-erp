#gui.py
from flaskwebgui import FlaskUI
from core.wsgi import application as app

if __name__ == "__main__":
    FlaskUI(
        app=app,
        server="django",
        port=8000
        ).run()