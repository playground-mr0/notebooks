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
    sb.open("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AcMMx-cjZweVabYIsP5kUsVfuS6Q7T-dvar6uwFzZ1cFMCcsY1SAYKnCeRPWRJZRzxTvRgRbggrbvA&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1647635945%3A1731316778837491&ddm=1")
    #sb.open("https://www.google.com/gmail/about/")
    #https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AcMMx-cjZweVabYIsP5kUsVfuS6Q7T-dvar6uwFzZ1cFMCcsY1SAYKnCeRPWRJZRzxTvRgRbggrbvA&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1647635945%3A1731316778837491&ddm=1
    #sb.click('a[data-action="sign in"]')
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
    
    wait = WebDriverWait(sb, 120)

    def find_md_icon_text():
        colab_connect_button = sb.find_element(By.CSS_SELECTOR, "colab-connect-button")
        print("Found colab connect_button")

        # Use JavaScript to get the Shadow DOM and print its content
        shadow_root_content = sb.execute_script("""
            const shadowHost = arguments[0];
            const shadowRoot = shadowHost.shadowRoot;
            if (shadowRoot) {
                return shadowRoot.innerHTML;
            } else {
                return "No Shadow DOM found";
            }
        """, colab_connect_button)

        print("Shadow DOM Content:")
        print(shadow_root_content)

        # Use JavaScript to fetch the 'md-icon' element's text content
        interval = 1
        number_checks = 20

        md_icon_text_final = "not_done"
        
        for i in range(number_checks):
            md_icon_text = sb.execute_script("""
                const shadowHost = arguments[0];
                const shadowRoot = shadowHost.shadowRoot;
                if (shadowRoot) {
                    const mdIcon = shadowRoot.querySelector('md-icon');
                    return mdIcon ? mdIcon.textContent.trim() : "md-icon not found";
                } else {
                    return "No Shadow DOM found";
                }
            """, colab_connect_button)

            time.sleep(interval)

            if i == 0:
                md_icon_text_final = md_icon_text
            elif md_icon_text!="done":
                md_icon_text_final = md_icon_text

        #print("\nmd-icon Text Content:")
        #print(md_icon_text)  

        return md_icon_text  

    def is_notebook_busy():
        try:

            # 1st Approach - When the status was given on the pages bottom bar
            # Access the shadow DOM root
            '''
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
            '''

            # 2nd approach - we go for the success icon on the top right corner of the page next to the RAM/Disk consumption
            
            md_icon_text = find_md_icon_text()

            if md_icon_text == "done":
                return True
            else:
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
    
    sb.send_keys("body", Keys.CONTROL + "e")
    print("Pressed CTRL+E already")
    '''
    print("Saving copy in Github with custom keyboard shortcut")
    time.sleep(10)
    sb.click("mwc-button[dialogaction='ok']")
    input()
    '''
    
    print("End of commands")

    #while True:
    #    pass
    
