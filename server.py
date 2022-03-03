# ...server.py
from flask_app import app
from flask_app.controllers import articles_controller, users_controller


if __name__ == "__main__":
    app.run(debug=True)