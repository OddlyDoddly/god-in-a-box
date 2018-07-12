from screens.Screen import Screen
from screens.AppsScreen import AppsScreen

from PIL import Image
from PIL import ImageDraw

import os

class EyeScreen(Screen):
    def __init__(self, display, runner):
        super().__init__(display, runner)
        self.frame_index = 0
        self.frames = [
            Image.open(os.path.join(os.path.dirname(__file__), '../animation/eye/f1.pbm')).convert('1'),
            Image.open(os.path.join(os.path.dirname(__file__), '../animation/eye/f3.pbm')).convert('1'),
            Image.open(os.path.join(os.path.dirname(__file__), '../animation/eye/f5.pbm')).convert('1'),
            Image.open(os.path.join(os.path.dirname(__file__), '../animation/eye/f7.pbm')).convert('1'),
            Image.open(os.path.join(os.path.dirname(__file__), '../animation/eye/f8.pbm')).convert('1'),
            Image.open(os.path.join(os.path.dirname(__file__), '../animation/eye/f9.pbm')).convert('1'),
            Image.open(os.path.join(os.path.dirname(__file__), '../animation/eye/f11.pbm')).convert('1'),
            Image.open(os.path.join(os.path.dirname(__file__), '../animation/eye/f13.pbm')).convert('1'),
            Image.open(os.path.join(os.path.dirname(__file__), '../animation/eye/f15.pbm')).convert('1'),
        ]
        self.messages = [
            {
                'type': 'message',
                'message': 'Welcome back, Dylan.'
            },
            {
                'type': 'prompt',
                'message': 'What should I do?',
                'options': ['APP', 'SCRIPT', 'WORK', 'NETWORK'],
                'actions': [self.load_app_screen, self.load_app_screen, self.load_app_screen, self.set_message_index],
                'args': [tuple(), tuple(), tuple(), tuple([2])]
            },
            {
                'type': 'prompt',
                'message': 'Your Network:',
                'options': ['FRIENDS', 'INVITES', 'ALERTS', 'Back'],
                'actions': [self.set_message_index, self.set_message_index, self.set_message_index, self.set_message_index],
                'args': [tuple([1]), tuple([1]), tuple([1]), tuple([1])]
            },
        ]
        self.message_index = 0
        self.message_is_drawn = False
        self.message_character_index = 0

        self.in_prompt = False
        self.prompt_selection = 0

    def draw(self, image=None):
        image = self.frames[self.frame_index].copy()
        draw = ImageDraw.Draw(image)
        message = self.get_message()

        if self.messages[self.message_index]['type'] == 'prompt':
            draw.text((8, 2), message, fill=1)

            if self.message_is_drawn:
                self.in_prompt = True
                draw_offset = 0
                option_index = 0
                for option in self.messages[self.message_index]['options']:
                    draw_option = option

                    if option_index == self.prompt_selection:
                        draw_option = '> ' + draw_option

                    if option_index % 2 == 0:
                        draw.text((8, (self.height - 20) + draw_offset), draw_option, fill=1)
                    else:
                        draw.text((self.width - (len(draw_option)*8), (self.height - 20) + draw_offset),
                                  draw_option, fill=1)
                        draw_offset += 8

                    option_index += 1
        else:
            draw.text((8, self.height - 16), message, fill=1)

        super().draw(image)

        self.frame_index += 1
        if self.frame_index >= len(self.frames):
            self.frame_index -= 1

            if not self.message_is_drawn:
                self.frame_index = 0

    def on_input_press(self, control_code):
        if control_code == 'a' and self.message_is_drawn:
            if self.in_prompt and self.message_is_drawn:
                self.in_prompt = False
                args = self.messages[self.message_index]['args'][self.prompt_selection]
                return self.messages[self.message_index]['actions'][self.prompt_selection](*args)

            self.message_index += 1
            if self.message_index >= len(self.messages):
                self.message_index = 0

            self.message_is_drawn = False

        if self.messages[self.message_index]['type'] == 'prompt':
            if control_code == 'l' and self.in_prompt and self.message_is_drawn:
                self.prompt_selection -= 1

            if control_code == 'r' and self.in_prompt and self.message_is_drawn:
                self.prompt_selection += 1

            if control_code == 'u' and self.in_prompt and self.message_is_drawn:
                self.prompt_selection -= 2

            if control_code == 'd' and self.in_prompt and self.message_is_drawn:
                self.prompt_selection += 2

            if self.prompt_selection < 0:
                self.prompt_selection = 0
            elif self.prompt_selection >= len(self.messages[self.message_index]['options']):
                self.prompt_selection = len(self.messages[self.message_index]['options']) - 1

    def get_message(self):
        if not self.message_is_drawn:
            message = self.messages[self.message_index]['message']
            message_part = message[:self.message_character_index]
            self.message_character_index += 1

            if self.message_character_index >= len(message):
                self.message_is_drawn = True
                self.message_character_index = 0

            return message_part
        else:
            return self.messages[self.message_index]['message']

    def set_message_index(self, value):
        self.message_index = value
        self.in_prompt = False
        self.message_is_drawn = False
        self.message_character_index = 0

    def load_app_screen(self):
        self.runner.set_screen(AppsScreen(self.display, self.runner, self))

