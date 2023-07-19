from flask import Flask, render_template, request
import pdfModule, qrModule, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    
    # Combine form data into a single string
    qr_data = f"Name: {fullname}, Email: {email}, Phone: {phone}"
    
    qrModule.generate_qr(qr_data,fullname)

    pdfName = pdfModule.create_pdf(fullname)

    with open(pdfName, 'rb') as file:
        pdf_data = file.read()
    
    os.remove(pdfName)
    return pdf_data, 200, {'Content-Type': 'application/pdf'}


if __name__ == "__main__":
    app.run(debug=True)