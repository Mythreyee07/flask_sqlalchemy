from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1/flask_project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


if __name__ == "__main__":
    app.run(debug=True)
