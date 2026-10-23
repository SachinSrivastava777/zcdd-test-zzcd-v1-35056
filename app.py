import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory todo list (resets when server restarts)
todos = []

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task", "").strip()
    if task:
        todos.append({"task": task, "done": False})
    return redirect(url_for("home"))

@app.route("/toggle/<int:idx>", methods=["POST"])
def toggle(idx):
    if 0 <= idx < len(todos):
        todos[idx]["done"] = not todos[idx]["done"]
    return redirect(url_for("home"))

@app.route("/delete/<int:idx>", methods=["POST"])
def delete(idx):
    if 0 <= idx < len(todos):
        todos.pop(idx)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", "5000")), host="0.0.0.0")
