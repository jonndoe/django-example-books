from PIL import Image, ImageDraw, ImageFont


class Watermark(object):
    def process(self, img):
        try:
            # For Linux
            font = ImageFont.truetype("DejaVuSans.ttf", 200)
        except Exception:
            print("No font DejaVuSans; use default instead")
            # For others
            font = ImageFont.load_default()
        #font = ImageFont.truetype("fonts/arialbd.ttf",40)
        #fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf',15)
        draw = ImageDraw.Draw(img)
        draw.text((200,100), "BOOKS STORE",font=font, fill=('#f0f0f0'))
        #draw.line((0, 0) + img.size, fill=128)
        #draw.line((0, img.size[1], img.size[0], 0), fill=128)
        return img


class Watermark_opacity(object):
    def process(self, img):
        base = img.convert('RGBA')
        width, height = base.size

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new('RGBA', base.size, (153, 152, 152, 150))

        # get a font
        #fnt = ImageFont.load_default(50).font
        try:
            # For Linux
            fnt = ImageFont.truetype("DejaVuSans.ttf", 10)
        except Exception:
            print("No font DejaVuSans; use default instead")
            # For others
            fnt = ImageFont.load_default()
        # get a drawing context
        d = ImageDraw.Draw(txt)

        x = width / 2
        y = height / 2

        # draw text, half opacity
        d.text((x, y), "BooksStore", font=fnt, fill=(255, 200, 255, 300))
        txt = txt.rotate(15)

        img = Image.alpha_composite(base, txt)
        return img


class WatermarkText(object):
    def process(self, img):
        # make the image editable
        drawing = ImageDraw.Draw(img)
        black = (3, 8, 12)
        font = ImageFont.truetype("Times_New_Roman.ttf", 50)
        drawing.text((60, 60), text="WaterMark", fill=black, font=font)
        return img
