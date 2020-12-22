from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from flask import send_file

from utils.endpoint import Endpoint, setup
from utils.textutils import wrap, render_text_with_emoji


@setup
class EmergencyMeeting(Endpoint):
    params = ['text']

    def generate(self, avatars, text, usernames, kwargs):
        base = Image.open('assets/emergencymeeting/emergencymeeting.bmp')
        font = ImageFont.truetype('assets/fonts/medium.woff', size=33)
        canv = ImageDraw.Draw(base)
        if len(text) >= 140:
            text = text[:137] + "..."
        text = wrap(font, text, 750)
        render_text_with_emoji(base, canv, (0, 0), text, font=font, fill='Black')

        base = base.convert('RGB')
        b = BytesIO()
        base.save(b, format='jpeg')
        b.seek(0)
        return send_file(b, mimetype='image/jpeg')
