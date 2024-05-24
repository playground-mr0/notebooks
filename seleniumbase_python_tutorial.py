import time
from seleniumbase import SB
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    #sb.open("https://colab.research.google.com/drive/1X7MLy8L60uKzDU68Z7Y-F42ZKW-5Rm6R#scrollTo=bK40_0ZPYkZf") #simple_prints_notebook
    sb.open("https://colab.research.google.com/drive/1UM7kg8JK3Y6B7pGyuvVOl6yUq0b_kk2_#scrollTo=Xr3zWNwUeoaG") #mr0_FID_notebook
    
    time.sleep(10)
    
    sb.click("body")
    sb.send_keys("body", Keys.CONTROL + Keys.F9)
    print("Pressed CTRL+F9 already")
    
    wait = WebDriverWait(sb, 60)
    def is_notebook_busy():
        try:

            # Access the shadow DOM root
            colab_status_bar = sb.find_element(By.CSS_SELECTOR, "colab-status-bar")
            print("Found colab status bar")
            
            print("Attempting to access shadow root of colab-status-bar...")
            shadow_root = sb.execute_script('return arguments[0].shadowRoot', colab_status_bar)
            print("Shadow root of colab-status-bar accessed.")
            
            print("Attempting to locate md-icon with class 'success' inside the shadow root...")
            icon = shadow_root.find_element(By.CSS_SELECTOR, "md-icon.success")
            print("Success icon found.")

            # Check if the class contains 'success'
            if 'success' in icon.get_attribute('class'):
                return True
            return False
        except:
            return False

    # Wait for the notebook to finish running all cells
    while not is_notebook_busy():
        print("Not found")
        time.sleep(5)  # Wait for a few seconds before checking again
    print("SUCCESS and end it")
    
    
    #=============================
    #   Save in Google drive
    #=============================
    sb.send_keys("body", Keys.CONTROL + "s")
    print("Pressed CTRL+S already")
    time.sleep(10)
    
    #=============================
    #   Download notebook
    #=============================
    sb.send_keys("body", Keys.CONTROL + "a")
    print("Pressed CTRL+A already")
    time.sleep(20)
    
    #=============================
    #   Save in Github
    #=============================
    '''
    sb.send_keys("body", Keys.CONTROL + "e")
    print("Pressed CTRL+E already")
    print("Saving copy in Github with custom keyboard shortcut")
    time.sleep(10)
    sb.click("mwc-button[dialogaction='ok']")
    input()
    '''
    
    print("End of commands")

    #while True:
    #    pass
    
