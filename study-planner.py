from flask import Flask, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task", "").strip()
        if task:
            tasks.append(task)
        return redirect("/")

    task_list = "".join(
        f"<li>{task}</li>" for task in tasks
    )

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Study Planner</title>
        <style>
            body {{ font-family: Arial; max-width: 600px;
                   margin: 40px auto; background: #f0f4f8; }}
            h1 {{ color: #234; }}
            input, button {{ padding: 10px; }}
            li {{ margin: 10px 0; }}
        </style>
    </head>
    <body>
        <h1>Student Study Planner</h1>
        <p>Add a task you want to study.</p>
        <form method="POST">
            <input name="task" placeholder="e.g. Revise Python"
                   required>
            <button type="submit">Add Task</button>
        </form>
        <h2>My Study Tasks</h2>
        <ul>{task_list}</ul>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)