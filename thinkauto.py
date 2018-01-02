import pyautogui as pg

#autoSendTrue()
#autoSendFalse()
#findDirWords()
#FindDirColor()

isAutoSend = False


def filler():
    pass

def checkAmount(func=filler):
    if pg.locateOnScreen("img/negone.png"):
        return "negOne"
    elif pg.locateOnScreen("img/posone.png"):
        return "posOne"
    else:
        result = findDirWords()
        if result == "long":
            print("more than one positive probably, reset")
            flattenTrade()
            buyMarket()
        elif result == "short":
            print("more than one short probably, reset")
            flattenTrade()
            sellMarket()
        elif result == "flat":
            return "flat"

def buyMarket():
    global isAutoSend;
    if isAutoSend == False:
        autoSendTrue(buyMarket)
        return        
    x,y = pg.locateCenterOnScreen("img/buymarketBtn.png")
    pg.click(x,y)
    print("BOT at market")

def sellMarket():
    global isAutoSend;
    if isAutoSend == False:
        autoSendTrue(sellMarket)
        return        
    x,y = pg.locateCenterOnScreen("img/sellmarketBtn.png")
    pg.click(x,y)
    print("SELL at market")

def flattenTrade():
    global isAutoSend;
    if isAutoSend == False:
        autoSendTrue(flattenTrade)
        return        
    x,y = pg.locateCenterOnScreen("img/flattenBtn.png")
    pg.click(x,y)
    print("FLATTEN")
    

def findDirColor():
    x,y = pg.locateCenterOnScreen("img/PosLoc.png")
    pg.click(x+36,y)
    col = pg.pixel(x+36,y)
    if col == (10, 96, 23):
        return "green"
    elif col == (255, 95, 95):
        return "red"
    
def findDirWords():
    if pg.locateOnScreen("img/PosLong.png",grayscale=True):
        return "long"
    elif pg.locateOnScreen("img/PosShort.png",grayscale=True):
        return "short"
    elif pg.locateOnScreen("img/posFlat.png",grayscale=True):
        return "flat"
    else:
        return False


def accessDropDown(func=filler):
    try:
        drop = pg.locateOnScreen("img/dropDownArrow.png")
        x,y = pg.center(drop)
        pg.click(x,y)
    except:
        drop = pg.locateOnScreen("img/MenuDropped.png")
        if drop:
            print("menu dropped")
    func()

def autoSendTrue(func=filler):
    global isAutoSend;
    try:
        btn = pg.locateOnScreen("img/autoSendOff.png")
        x,y = pg.center(btn)
        pg.click(x,y)
        print("clicked to turn on")
        isAutoSend = True
    except:
        btn = pg.locateOnScreen("img/autoSendOn.png")
        if btn:
            print("its already on")
            isAutoSend = True
        else:
            accessDropDown(autoSendTrue)
    func()
            
def autoSendFalse(func=filler):
    global isAutoSend;
    try:
        btn = pg.locateOnScreen("img/autoSendOn.png")
        x,y = pg.center(btn)
        pg.click(x,y)
        print("clicked to turn off")
        isAutoSend = False;
    except:
        btn = pg.locateOnScreen("img/autoSendOff.png")
        if btn:
            print("its already off")
            isAutoSend = False
        else:
            accessDropDown(autoSendFalse)
    func()
        
