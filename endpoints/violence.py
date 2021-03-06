from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from flask import send_file

from utils.endpoint import Endpoint, setup
from utils.textutils import render_text_with_emoji, wrap


@setup
class Violence(Endpoint):
    params = ["text"]

    def generate(self, avatars, text, usernames, kwargs):
        base = Image.open("assets/violence/violence.jpg")
        font = ImageFont.truetype("assets/fonts/arimobold.ttf", size=24)
        canv = ImageDraw.Draw(base)
        render_text_with_emoji(
            base, canv, (355, 0), wrap(font, text, 270), font, "black"
        )

        base = base.convert("RGB")
        b = BytesIO()
        base.save(b, format="jpeg")
        b.seek(0)
        return send_file(b, mimetype="image/jpeg")
