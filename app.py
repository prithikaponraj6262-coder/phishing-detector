from flask import Flask, render_template, request

app = Flask(__name__)

def check_url(url):
    score = 0

    if "@" in url:
        score += 2
    if "-" in url:
        score += 1
    if "http://" in url:
        score += 2
    if "login" in url or "verify" in url:
        score += 2
    if len(url) > 75:
        score += 1

    if score >= 4:
        return "🔴 High Risk Phishing Website"
    elif score >= 2:
        return "🟡 Suspicious Website"
    else:
        return "🟢 Safe Website"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        result = check_url(url)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
