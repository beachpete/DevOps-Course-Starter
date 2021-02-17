from flask import Flask

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return 'Hello Pete!'


if __name__ == '__main__':
    app.run()
