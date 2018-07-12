from .Screen import Screen
from screens.MainMenu import EyeScreen

from PIL import Image

import time
import os

class SplashScreen(Screen):
    def __init__(self, display, runner):
        super().__init__(display, runner)

    def draw(self, image=None):
        image = Image.open(os.path.join(os.path.dirname(__file__), '../boot.ppm')).convert('1')
        super().draw(image)
        time.sleep(5)
        self.runner.set_screen(EyeScreen(self.display, self.runner))
