from screens.SplashScreen import SplashScreen

import RPi.GPIO as GPIO
from threading import Thread
import time

# Input pins:
L_pin = 27
R_pin = 23
C_pin = 4
U_pin = 17
D_pin = 22

A_pin = 5
B_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(L_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(R_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(U_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(D_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(C_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class Runner:
    def __init__(self, display):
        self.display = display
        self.loaded_screen = SplashScreen(self.display, self)
        self.input_thread = Thread(target=self.run_input)

    def run(self):
        self.input_thread.start()
        while(1):
            self.loaded_screen.draw()

    def run_input(self):
        while(1):
            self.check_input()
            time.sleep(.2)

    def set_screen(self, screen):
        self.loaded_screen.clear_screen()
        self.loaded_screen = screen

    def check_input(self):

        if GPIO.input(U_pin):
            self.loaded_screen.on_input_release("u")
        else:
            self.loaded_screen.on_input_press("u")

        if GPIO.input(L_pin):
            self.loaded_screen.on_input_release("l")
        else:
            self.loaded_screen.on_input_press("l")

        if GPIO.input(R_pin):
            self.loaded_screen.on_input_release("r")
        else:
            self.loaded_screen.on_input_press("r")

        if GPIO.input(D_pin):
            self.loaded_screen.on_input_release("d")
        else:
            self.loaded_screen.on_input_press("d")

        if GPIO.input(C_pin):
            self.loaded_screen.on_input_release("c")
        else:
            self.loaded_screen.on_input_press("c")

        if GPIO.input(A_pin):
            self.loaded_screen.on_input_release("b")
        else:
            self.loaded_screen.on_input_press("b")

        if GPIO.input(B_pin):
            self.loaded_screen.on_input_release("a")
        else:
            self.loaded_screen.on_input_press("a")

        # Restarter
        if not GPIO.input(B_pin) and not GPIO.input(A_pin) and not GPIO.input(C_pin):
            self.loaded_screen = SplashScreen(self.display, self)
