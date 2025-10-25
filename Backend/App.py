from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder="../Frontend/templates")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# ...existing code...


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
