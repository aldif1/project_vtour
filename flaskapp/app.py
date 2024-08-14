from flask import Flask, render_template,session,send_from_directory
import os
app = Flask(__name__)
app.secret_key = 'c~maeri2394i9302/;0a1'  
project_root = os.path.dirname(os.path.abspath(__file__))
parent_root = os.path.dirname(project_root)

@app.route('/custom_static/<path:filename>')
def custom_static(filename):
    return send_from_directory(parent_root, filename)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/tegal")
def tegal():
    return render_template("index.html")
@app.route("/semarang")
def semarang():
    return render_template("index.html")
@app.route("/tegal/pai")
def tegal_pai():
    return render_template("index.html")
@app.route("/semarang/sam_po_kong")
def semarang_sam_po_kong():
    return render_template("index.html")
@app.route("/semarang/kota_lama")
def semarang_kota_lama():
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
