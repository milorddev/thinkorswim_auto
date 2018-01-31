from PIL import Image
import pyautogui as pg

import pyocr
import pyocr.builders


think = pg.getWindow("thinkorswim [build 1920]")
pos = think.get_position()
reg = (round(pos[0]+(pos[2]-pos[0])*0.5416),
       round(pos[1]+(pos[3]-pos[1])*0.1768),
       round((pos[2]-pos[0])*0.1287),
       round((pos[3]-pos[1])*0.7889))
print(reg)
img = pg.screenshot(region= reg)
img.show()

'''

buyx,buyy = pg.locateCenterOnScreen('img/buysignal.png', region=(pos[0]+(pos[2]-pos[0])*0.5416,
                                                                         pos[1]+(pos[3]-pos[1])*0.1368,
                                                                         (pos[2]-pos[0])*0.1287,
                                                                         (pos[3]-pos[1])*0.8189))


threshold = 99

x,y = pg.locateCenterOnScreen('img/avgPrice.png')
img = pg.screenshot(region=(x + 18,y - 12,60,20))
img = img.convert('L')
width, height = img.size
img = img.resize((width*2,height*2),Image.ANTIALIAS)
img = img.point(lambda p:p > threshold and 255)
img.show()
#img.save("tempAvgPrice.png")

tools = pyocr.get_available_tools()[0]
text = tools.image_to_string(img,builder=pyocr.builders.DigitBuilder())
print(text)
'''
