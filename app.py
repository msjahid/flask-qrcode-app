from flask import Flask, render_template, request, send_from_directory, send_file
from pathlib import Path
import qrcode
import os
app = Flask(__name__, static_url_path='/static')

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    linkData = request.form['url_link']
    qr.add_data(linkData)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    return render_template('index.html')


# @app.route('/download/<path:filename>', methods=['GET', 'POST'])
# def downloadFile(filename):
#     downloads = str(os.path.join(Path.home(), "Downloads"))
#     return send_from_directory(directory=downloads, filename=filename, as_attachment=True)

@app.route('/download')
def downloadFile():
    file = "qrcode.png"
    return send_file(file, as_attachment=True)


if __name__ == '__main__':
    app.run()
