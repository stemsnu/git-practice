#-*-coding: utf-8-*-
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "정태희싫어요"

@app.route("/index")
def index():
    return render_template("index.html", departments=[u"학술",u"봉사",u"대외교류"])


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=55555)
