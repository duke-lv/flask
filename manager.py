from flask import Flask
from config import DevConfig
from flask.ext.script import Manager, Server

app = Flask(__name__)
app.config.from_object(DevConfig)

manager = Manager(app)

manager.add_command(label="server", command=Server())

def make_shell_context():
    return dict(app=app)

@app.route("/")
def home():
    return '<h1>hello world</h1>'
if __name__ == '__main__':
    # app.run()
    manager.run()