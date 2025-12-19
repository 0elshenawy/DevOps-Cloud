from flask import Flask, request, redirect, url_for, render_template, flash
from pathlib import Path
import os
import urllib.parse

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")

DATA_DIR = "./data"
Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

def user_file(username):
    # sanitize simple: percent-encode username to avoid path injection
    safe = urllib.parse.quote(username, safe='')
    return os.path.join(DATA_DIR, f"{safe}.txt")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    if not username or not password:
        flash("Please provide username and password", "error")
        return redirect(url_for("index"))

    # Demo: store a single users file (append). In production, hash passwords!
    uf = user_file(username)
    try:
        with open(uf, "a") as f:
            f.write(f"__CREATED_USER__|{username}|{password}\n")
    except Exception as e:
        flash(f"Error saving user: {e}", "error")
        return redirect(url_for("index"))

    # redirect to todo page with username in query param
    return redirect(url_for("todo") + f"?user={urllib.parse.quote(username)}")

@app.route("/todo", methods=["GET"])
def todo():
    username = request.args.get("user", "").strip()
    if not username:
        flash("No user specified", "error")
        return redirect(url_for("index"))

    uf = user_file(username)
    todos = []
    if os.path.exists(uf):
        try:
            with open(uf, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    # ignore created-user markers
                    if line.startswith("__CREATED_USER__|"):
                        continue
                    todos.append(line)
        except Exception as e:
            flash(f"Error reading user file: {e}", "error")

    return render_template("todo.html", username=username, todos=todos)

@app.route("/todo/add", methods=["POST"])
def todo_add():
    username = request.form.get("user", "").strip()
    item = request.form.get("item", "").strip()
    if not username or not item:
        flash("Missing user or item", "error")
        return redirect(url_for("index"))

    uf = user_file(username)
    try:
        with open(uf, "a") as f:
            f.write(f"{item}\n")
    except Exception as e:
        flash(f"Error writing todo: {e}", "error")

    return redirect(url_for("todo") + f"?user={urllib.parse.quote(username)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)

