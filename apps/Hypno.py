from screens.Screen import Screen

from PIL import Image
import os


class HypnoScreen(Screen):
    def __init__(self, display, runner, sender):
        super().__init__(display, runner)
        self.sender = sender
        self.counter = 2
        self.frame1 = Image.open(os.path.join(os.path.dirname(__file__), '../animation/hypno/f1.ppm')).convert('1')
        self.frame2 = Image.open(os.path.join(os.path.dirname(__file__), '../animation/hypno/f2.pbm')).convert('1')

    def draw(self, image=None):
        if self.counter % 2:
            super().draw(self.frame1)
        else:
            super().draw(self.frame2)

        self.counter += 1

    def on_input_press(self, control_code):
        if control_code == 'b':
            self.runner.set_screen(self.sender)
