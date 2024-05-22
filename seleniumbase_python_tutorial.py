import time
from seleniumbase import SB
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# nothing

with SB(uc=True) as sb:
    
    #=============================
    #   Log in to Google account
    #=============================
    sb.open("https://www.google.com/gmail/about/")
    sb.click('a[data-action="sign in"]')
    sb.type('input[type="email"]', "playgroundmr0@gmail.com")
    sb.click('button:contains("Next")')
    sb.type('input[type="password"]', "X338LrDt$@:1")
    sb.click('button:contains("Next")')
    
    time.sleep(10)
   
    #=============================
    #   Open and run notebook
    #=============================
    sb.open("https://colab.research.google.com/drive/1X7MLy8L60uKzDU68Z7Y-F42ZKW-5Rm6R#scrollTo=bK40_0ZPYkZf")
    
    time.sleep(30)
    
    sb.click("body")
    # Simulate Ctrl+F9
    sb.send_keys("body", Keys.CONTROL + Keys.F9)
    print("Pressed CTRL+F9 already")
    time.sleep(30)
    sb.send_keys("body", Keys.CONTROL + "s")
    print("Pressed CTRL+S already")
    time.sleep(10)
    sb.send_keys("body", Keys.CONTROL + "e")
    print("Pressed CTRL+E already")
    print("Saving copy in Github with custom keyboard shortcut")
    time.sleep(10)
    sb.click("mwc-button[dialogaction='ok']")
    input()
    print("End of commands")

    #while True:
    #    pass
    

