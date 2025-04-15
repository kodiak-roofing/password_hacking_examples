# fake_login_server.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded "correct" credentials
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "hunter2"

# Simple HTML form
HTML = """
<!doctype html>
<title>Login</title>
<h2>Login Page</h2>
<form method=post>
  Username: <input type=text name=username><br>
  Password: <input type=password name=password><br>
  <input type=submit value=Login>
</form>
{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if (request.form["username"] == CORRECT_USERNAME and
                request.form["password"] == CORRECT_PASSWORD):
            return "<h1>Login Successful!</h1>"
        else:
            error = "Invalid username or password."
    return render_template_string(HTML, error=error)


if __name__ == "__main__":
    app.run(debug=True)
