import pyautogui as pg
import time
import datetime

#autoSendTrue()
#autoSendFalse()
#findDirWords()
#FindDirColor()
#magnify(numOfRepeats)
#unmagnify(numofRepeats)
#checkAmount()
#setChart(type,interval,period)
#buyMarket()
#sellMarket()
#flattenTrade()

isAutoSend = False

interval = ['today','WTD','1 day','2 day','3 day','4 day','5 day','10 day','15 day',
            '20 day','30 day','90 day','180 day','360 day','YTD','1 month',
            '3 month','6 month','9 month','1 year','2 year','3 year','4 year',
            '5 year','10 year','15 year','20 year','max']

dayPeriod = ['day','2 day','3 day','4 day','week ','month']

think = pg.getWindow("thinkorswim [build 1912]")

loop = True
sleepTime = 15

trades = []

def filler():
    pass

def checkStrategy():
    global think,trades;
    magnify(8)
    pos = think.get_position()
    try:
        buyx,buyy = pg.locateCenterOnScreen('img/buysignal.png', region=(pos[0]+(pos[2]-pos[0])*0.5416,
                                                                         pos[1]+(pos[3]-pos[1])*0.1368,
                                                                         (pos[2]-pos[0])*0.1287,
                                                                         (pos[3]-pos[1])*0.8189))
        if buyx:
            print("buy signal!",buyx,buyy)
            currentDir = checkAmount()
            if currentDir == "negOne":
                print("reversing!")
                reverseTrade()
                tradestring = "BUY +1 at " + str(datetime.datetime.now()).split('.')[0]
                trades.append(tradestring)
            elif currentDir == "posOne":
                print("do nothing, already that direction")
            elif currentDir == "flat":
                print("not in, buy")
                buyMarket()
                tradestring = "BUY +1 at " + str(datetime.datetime.now()).split('.')[0]
                trades.append(tradestring)
    except:
        try:
            sellx,selly = pg.locateCenterOnScreen('img/sellsignal.png', region=(pos[0]+(pos[2]-pos[0])*0.5416,
                                                                             pos[1]+(pos[3]-pos[1])*0.1368,
                                                                             (pos[2]-pos[0])*0.1287,
                                                                             (pos[3]-pos[1])*0.8189))
            if sellx:
                print("sell signal!",sellx,selly)
                currentDir = checkAmount()
                if currentDir == "posOne":
                    print("reversing!")
                    reverseTrade()
                    tradestring = "SELL +1 at " + str(datetime.datetime.now()).split('.')[0]
                    trades.append(tradestring)
                elif currentDir == "negOne":
                    print("do nothing, already that direction")
                elif currentDir == "flat":
                    print("not in, sell")
                    sellMarket()
                    tradestring = "SELL +1 at " + str(datetime.datetime.now()).split('.')[0]
                    trades.append(tradestring)

        except:
            print("nothing there")




def magnify(times=1):
    pos = think.get_position()    
    try:
        x,y = pg.locateCenterOnScreen('img/magnifyBtn.png', region=(pos[0],
                                                            pos[1]+(pos[3]-pos[1])*0.80,
                                                            pos[2]-pos[0],
                                                            (pos[3]-pos[1])*0.20))
        for i in range(times):
            pg.click(x,y)
    except:
        print("already max mag")

def unmagnify(times=1):
    try:
        x,y = pg.locateCenterOnScreen('img/unmagnifyBtn.png', region=(pos[0],
                                                            pos[1]+(pos[3]-pos[1])*0.80,
                                                            pos[2]-pos[0],
                                                            (pos[3]-pos[1])*0.20))
        for i in range(times):
            pg.click(x,y)
    except:
        print("already max unmag")            

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
            return "posOne"
        elif result == "short":
            print("more than one short probably, reset")
            flattenTrade()
            sellMarket()
            return "negOne"
        elif result == "flat":
            return "flat"

def setChart(type='time' , inti='5 day', period='0001'):
    type = str(type)
    inti = str(inti)
    period = str(period)
    global interval
    x,y = pg.locateCenterOnScreen("img/settingsBtn.png")
    pg.click(x,y)
    time.sleep(1)
    x,y = pg.locateCenterOnScreen("img/timeAxisBtn.png")
    pg.click(x,y)
    time.sleep(0.3)
    x,y = pg.locateCenterOnScreen("img/aggregationType.png")
    pg.click(x+100,y)
    pg.press(['up','up','up'])
    if type.lower() == 'time':
        pg.press('down')
    elif type.lower() == 'range':
        pg.press(['down','down'])
    pg.click(x,y)

    x,y = pg.locateCenterOnScreen("img/timeInterval.png")
    pg.click(x+100,y)
    pg.press(['pgup','pgup','pgup'])
    count = 0;
    for index,i in enumerate(interval):
        if inti in i:
            count = index
            break
    print(count)
    for i in range(count):
        pg.press('down')
    pg.click(x,y)

    global dayPeriod;
    x,y = pg.locateCenterOnScreen("img/aggregationPeriod.png")
    pg.click(x+100,y)
    #in the years section
    if count > 13:
        periodCount = 0
        pg.press(['pgup','pgup','pgup'])
        for index, i in enumerate(dayPeriod):
            if period in i:
                periodCount = index
                break
        for i in range(periodCount):
            pg.press('down')
    else:
        pg.press(['right','right','right','right','right'])
        pg.press(['backspace','backspace','backspace','backspace','backspace'])
        pg.typewrite(period)
        pg.press('enter')
    pg.click(x,y)

    x,y = pg.locateCenterOnScreen("img/okSettings.png")
    pg.click(x,y)
    print("settings saved")

    
    
def reverseTrade():
    global isAutoSend;
    if isAutoSend == False:
        autoSendTrue(reverseTrade)
        return        
    x,y = pg.locateCenterOnScreen("img/reverseBtn.png")
    pg.click(x,y)
    print("REVERSE")    
    
        

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


def startTrading():
    global loop,sleepTime
    while(loop):
        print(str(datetime.datetime.now()).split('.')[0])
        checkStrategy()
        time.sleep(sleepTime)

startTrading()
