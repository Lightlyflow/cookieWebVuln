from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def home():
    isAdmin = request.cookies.get("admin")
    response = make_response(render_template("index.html"))
    if isAdmin is None:
        response.set_cookie("admin", "False")
    return response


@app.route("/login")
def login():
    isAdmin = request.cookies.get("admin")
    return render_template("login.html", admin=isAdmin)


if __name__ == '__main__':
    app.run()
