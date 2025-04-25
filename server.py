
from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/upscale', methods=['POST'])
def upscale():
    file = request.files['image']
    img = Image.open(file.stream)
    # Simulasi upscale 4x (pakai Real-ESRGAN asli di implementasi nyata)
    img = img.resize((img.width * 4, img.height * 4), Image.LANCZOS)
    output = io.BytesIO()
    img.save(output, format='PNG')
    output.seek(0)
    return send_file(output, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
