from screens.Screen import Screen

# Apps
from apps.Time import TimeScreen
from apps.DeviceInfo import InfoScreen
from apps.Hypno import HypnoScreen
from apps.Bitcoin import BitcoinScreen
from apps.RestartTerm import TermScreen
from apps.TakePicture import TakePicture

from PIL import Image
from PIL import ImageDraw


class AppsScreen(Screen):
    def __init__(self, display, runner, sender):
        super().__init__(display, runner)
        self.sender = sender
        self.clear_screen()
        self.cursor_index = 0
        self.real_index = 0
        self.scroll = 0

        self.apps = [
            {'name': 'Time Display', 'screen': TimeScreen},
            {'name': 'Device Info', 'screen': InfoScreen},
            {'name': 'Hypno Animation', 'screen': HypnoScreen},
            {'name': 'Bitcoin', 'screen': BitcoinScreen},
            {'name': 'Restart Term', 'screen': TermScreen},
            {'name': 'Camera', 'screen': TakePicture}
        ]

    def draw(self, image=None):
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        draw.rectangle((0, 0, self.width, 12), outline=0, fill=1)
        draw.text((4, 0), "Run an app: (A)", fill=0)

        draw.rectangle((0, 16 + (self.cursor_index * 16), self.width, 16 + (self.cursor_index * 16) + 16), outline=0, fill=1)

        draw_offset = 0
        i = 0
        for script in self.apps:
            if i >= self.scroll:
                if draw_offset == self.cursor_index:
                    draw.text((8, 16 + (draw_offset * 16)), script['name'], fill=0)
                else:
                    draw.text((8, 16 + (draw_offset * 16)), script['name'], fill=1)
                draw_offset += 1
            i += 1

        super().draw(image)

    def on_input_press(self, control_code):
        if control_code == 'b' and self.real_index < len(self.apps):
            self.runner.set_screen(self.sender)
        if control_code == 'a' and self.real_index < len(self.apps):
            self.run_script(self.apps[self.real_index])
        elif control_code == 'u':
            self.cursor_index -= 1
            self.real_index -= 1
        elif control_code == 'd' and self.real_index+1 < len(self.apps):
            self.cursor_index += 1
            self.real_index += 1

        if self.cursor_index > 2:
            self.cursor_index = 2
            self.scroll += 1
        elif self.cursor_index < 0:
            self.cursor_index = 0
            self.scroll -= 1

        if self.scroll < 0:
            self.scroll = 0

        if self.real_index < 0:
            self.real_index = 0

    def run_script(self, script):
        self.runner.set_screen(script['screen'](self.display, self.runner, self))
