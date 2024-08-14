from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/tegal")
def index():
    return render_template("index.html")
@app.route("/semarang")
def index():
    return render_template("index.html")
@app.route("/tegal/pai")
def index():
    return render_template("index.html")
@app.route("/semarang/sam_po_kong")
def index():
    return render_template("index.html")
@app.route("/semarang/kota_lama")
def index():
    return render_template("index.html")
@app.route("/semarang/goa_kreo")
def semarang_goa_kreo():
    return render_template("goa_kreo.html")
@app.route("/semarang/goa_kreo/vt")
def semarang_goa_kreo_vt():
    return render_template("goa_kreo/index.html")
@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")
if __name__ == "__main__":
    app.run(debug=True)
