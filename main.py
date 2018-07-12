import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from Runner import Runner

# Raspberry Pi pin configuration:
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

def main():
    try:
        display = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
        display.begin()

        runner = Runner(display)
        runner.run()

    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
