import board
import neopixel
import time
import colorsys

pixels = neopixel.NeoPixel(board.D12, 300)

while True:
        for i in range(300):
                hue = i / 300 * 360
                hsv = (hue / 360, 1.0, 1.0)
                rgb = colorsys.hsv_to_rgb(*hsv)
                color = tuple([int(c * 255) for c in rgb])
                pixels[i] = color
                time.sleep(0.001)

        for i in range(299, -1, -1):
                pixels[i] = (0, 0, 0)
                time.sleep(0.001)


