from flask import Flask, render_template,session,send_from_directory, request, jsonify
from flask_cors import CORS, cross_origin
import json
import os

app = Flask(__name__)

# Path ke file data.json
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

# Fungsi untuk membaca data dari file JSON
def read_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

# Fungsi untuk menulis data ke file JSON
def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

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
    data = read_data()
    data.append(new_feedback)
    write_data(data)
    return jsonify({"message": "Feedback saved successfully!"}), 200

@app.route('/lihat_review')
def lihat_review():
    data = read_data()
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