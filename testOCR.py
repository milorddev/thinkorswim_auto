from pytesseract import image_to_string
import pyautogui as pg
from PIL import Image
import time

x,y = pg.locateCenterOnScreen("img/avgPrice.png")
ig = pg.screenshot(region=(x+18,y-10,60,20))
text = image_to_string(ig)
print(text)
