from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        reply = f"أرسلت: {request.form.get('message')}"
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
