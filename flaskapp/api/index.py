from flask import Flask, render_template,session,send_from_directory, request, jsonify
from flask_cors import CORS, cross_origin
import json
import os

app = Flask(__name__)
data = [
    {
        "name": "John Doe",
        "feedback": "Situs ini sangat informatif dan user-friendly. Terima kasih!"
    },
    {
        "name": "Jane Smith",
        "feedback": "Saya menyarankan agar lebih banyak artikel ditambahkan setiap minggunya."
    }
]

@app.route('/api/feedback', methods=['POST'])
@cross_origin()
def save_feedback():
    name = request.json.get("name")
    feedback = request.json.get("feedback")
    
    # Contoh untuk menyimpan data ke file JSON
    new_feedback = {
        "name": name,
        "feedback": feedback
    }
    data.append(new_feedback)

    return jsonify({"message": "Feedback saved successfully!"}), 200

@app.route('/lihat_review')
def lihat_review():
    return jsonify(data)

@app.route('/')
def home():
    return 'Hello, World!'
@app.route("/tegal")
def tegal():
    return render_template("tegal.html")
@app.route("/semarang")
def semarang():
    return render_template("semarang.html")
@app.route("/tegal/pai")
def tegal_pai():
    return render_template("pai.html")
@app.route("/semarang/sam_po_kong")
def semarang_sam_po_kong():
    return render_template("sam_po_kong.html")
@app.route("/semarang/kota_lama")
def semarang_kota_lama():
    return render_template("kota_lama.html")
@app.route("/semarang/goa_kreo")
def semarang_goa_kreo():
    return render_template("goa_kreo.html")
@app.route("/semarang/goa_kreo/vt")
def semarang_goa_kreo_vt():
    return render_template("goa_kreo/index.html")
@app.route("/semarang/SAM_PO_KONG/vt")
def semarang_SAM_PO_KONG_vt():
    return render_template("SAM_PO_KONG/index.html")
@app.route("/semarang/kota_lama/vt")
def semarang_kota_lama_vt():
    return render_template("kota_lama/index.html")
@app.route("/tegal/pai/vt")
def tegal_pai_vt():
    return render_template("pai/index.html")
@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route('/about')
def about():
    return 'About'