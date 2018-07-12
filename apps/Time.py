from screens.Screen import Screen

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import time


class TimeScreen(Screen):
    def __init__(self, display, runner, sender):
        super().__init__(display, runner)
        self.sender = sender


    def draw(self, image=None):
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        draw.rectangle((0, 0, self.width, 12), outline=0, fill=1)
        draw.text((4, 0), "Current Time: ", fill=0)
        current_time = time.localtime()

        draw.text((8, 16), time.strftime('%a, %d %b %Y', current_time), fill=1)
        draw.text((8, 32), time.strftime('%H:%M:%S GMT', current_time), fill=1)

        super().draw(image)

    def on_input_press(self, control_code):
        if control_code == 'b':
            self.runner.set_screen(self.sender)
