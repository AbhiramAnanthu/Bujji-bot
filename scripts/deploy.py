from flask import Flask, request, jsonify
from script import extract_urls

app = Flask(__name__)


@app.route("/api/note", methods=["GET"])
def get_ktu_note():
    name = request.args.get("name")
    code = request.args.get("code")
    url = f"https://www.ktunotes.in/ktu-{name}-notes-{code}/"
    urls = extract_urls(url)
    return jsonify({"urls": urls}), 200


if __name__ == "__main__":
    app.run(debug=True)
