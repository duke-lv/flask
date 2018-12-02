from flask import Flask
from config import DevConfig
# from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
app.logger.debug(DevConfig)
# db = SQLALchemy(app)
@app.route("/")
def home():
    return '<h1>hello world</h1>'
if __name__ == '__main__':
    app.run()