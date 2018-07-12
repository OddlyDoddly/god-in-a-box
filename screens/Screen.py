class Screen:
    def __init__(self, display, runner):
        self.display = display
        self.runner = runner
        self.width = self.display.width
        self.height = self.display.height

        self.display.clear()
        self.display.display()

    def draw(self, image):
        self.display.clear()

        if image is not None:
            self.display.image(image)

        self.display.display()

    def clear_screen(self):
        self.display.clear()
        self.display.display()

    def on_input_release(self, control_code):
        pass

    def on_input_press(self, control_code):
        pass