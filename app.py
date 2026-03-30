from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/surat", methods=["POST"])
def surat():
    isi = request.form.get("surat")
    return render_template("surat.html", isi=isi)

@app.route("/baca")
def baca():
    isi = request.args.get("isi", "")
    return render_template("surat.html", isi=isi)

if __name__ == "__main__":
    app.run(debug=True)