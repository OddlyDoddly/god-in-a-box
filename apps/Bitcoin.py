from screens.Screen import Screen

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import urllib.request
import json
import time

class BitcoinScreen(Screen):
    def __init__(self, display, runner, sender):
        super().__init__(display, runner)
        self.sender = sender
        self.start_time = time.time()
        self.elapsed_time = 5

    def draw(self, image=None):
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        draw.rectangle((0, 0, self.width, 12), outline=0, fill=1)

        if self.elapsed_time % 5:
            url = urllib.request.urlopen("https://api.cryptowat.ch/markets/bitfinex/btcusd/price")
            data = url.read()
            encoding = url.info().get_content_charset('utf-8')
            btc_data = json.loads(data.decode(encoding))

            draw.text((4, 2), "BTC = $" + str(btc_data['result']['price']) + " USD ", fill=0)

            url = urllib.request.urlopen("https://api.cryptowat.ch/markets/bitstamp/ltcusd/price")
            data = url.read()
            encoding = url.info().get_content_charset('utf-8')
            ltc_data = json.loads(data.decode(encoding))

            draw.text((4, 18), "LTC = $" + str(ltc_data['result']['price']) + " USD ", fill=1)

            super().draw(image)

        self.elapsed_time += time.time() - self.start_time

    def on_input_press(self, control_code):
        if control_code == 'b':
            self.runner.set_screen(self.sender)
