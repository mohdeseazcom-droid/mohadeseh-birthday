from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save():
    name = request.form["name"]
    cake = request.form["cake"]
    wish = request.form["wish"]
    birth = request.form["birth"]

    with open("users.txt", "a", encoding="utf-8") as file:
        file.write(
            f"اسم: {name}\n"
            f"تاریخ تولد: {birth}\n"
            f"کیک مورد علاقه: {cake}\n"
            f"آرزو: {wish}\n"
            "------------------\n"
        )

    return "اطلاعات ثبت شد 🌸"
