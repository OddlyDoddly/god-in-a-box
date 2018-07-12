from screens.Screen import Screen

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import time
import subprocess


class InfoScreen(Screen):
    def __init__(self, display, runner, sender):
        super().__init__(display, runner)
        self.sender = sender

    def draw(self, image=None):
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)

        draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        draw.rectangle((0, 0, self.width, 12), outline=0, fill=1)
        draw.text((4, 0), "Device Info: ", fill=0)

        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell=True)
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell=True)
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell=True)
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell=True)

        # Write two lines of text.

        draw.text((2, 16), "IP: " + str(IP, 'utf-8'), fill=1)
        draw.text((2, 16 + 8), str(CPU, 'utf-8'), fill=1)
        draw.text((2, 16 + 16), str(MemUsage, 'utf-8'), fill=1)
        draw.text((2, 16 + 25), str(Disk, 'utf-8'), fill=1)

        super().draw(image)

    def on_input_press(self, control_code):
        if control_code == 'b':
            self.runner.set_screen(self.sender)
