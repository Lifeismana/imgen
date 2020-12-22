from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from flask import send_file

from utils.endpoint import Endpoint, setup
from utils.textutils import wrap, render_text_with_emoji


@setup
class Stroke(Endpoint):
    params = ["text"]

    def generate(self, avatars, text, usernames, kwargs):
        base = Image.open("assets/stroke/stroke.bmp")
        font = ImageFont.truetype("assets/fonts/verdana.ttf", size=12)
        canv = ImageDraw.Draw(base)
        text = wrap(font, text, 75)
        render_text_with_emoji(base, canv, (272, 287), text, font=font, fill="Black")

        base = base.convert("RGB")
        b = BytesIO()
        base.save(b, format="jpeg")
        b.seek(0)
        return send_file(b, mimetype="image/jpeg")
