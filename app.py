import qrcode
from flask import Flask, render_template, request
import base64
from io import BytesIO

app = Flask(__name__)

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color = "white", back_color = "black") 
    byte_stream = BytesIO()
    img.save(byte_stream, format="PNG")
    qr_code_base64 = base64.b64encode(byte_stream.getvalue()).decode('utf-8')
    return qr_code_base64

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code = None
    if request.method == 'POST':
        data_to_encode = request.form['data']
        qr_code = generate_qr_code(data_to_encode)

    return render_template('index.html', qr_code = qr_code)

if __name__ == "__main__":
    app.run()
