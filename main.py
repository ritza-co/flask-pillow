from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route("/")
def main():

    image = Image.open("flask-htmx.png")
    #image = img.rotate(45) rotate image by 45 degrees
    font = ImageFont.truetype("CollegiateBlackFLF.ttf", size=90)

    draw = ImageDraw.Draw(image)
    draw.text((500,100), "Hello World!", anchor="ms", font=font)

    obj = io.BytesIO()
    image.save(obj, format='png')
    obj.seek(0)

    return send_file(obj, mimetype='image/gif') 

if __name__ == "__main__":
    app.run()