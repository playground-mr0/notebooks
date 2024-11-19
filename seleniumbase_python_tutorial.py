import time
from seleniumbase import SB
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with SB(uc=True) as sb:

    done_running = False
    run_counter = 1
    successfull_signin = False

    while not(done_running) and run_counter <= 5:
        
        try:
            if not(successfull_signin):
                #=============================
                #   Log in to Google account
                #=============================
                sb.open("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AcMMx-cjZweVabYIsP5kUsVfuS6Q7T-dvar6uwFzZ1cFMCcsY1SAYKnCeRPWRJZRzxTvRgRbggrbvA&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1647635945%3A1731316778837491&ddm=1")#sb.open("https://www.google.com/gmail/about/")#https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AcMMx-cjZweVabYIsP5kUsVfuS6Q7T-dvar6uwFzZ1cFMCcsY1SAYKnCeRPWRJZRzxTvRgRbggrbvA&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1647635945%3A1731316778837491&ddm=1#sb.click('a[data-action="sign in"]')
                sb.type('input[type="email"]', "playgroundmr0@gmail.com")
                sb.click('button:contains("Next")')
                sb.type('input[type="password"]', "X338LrDt$@:1")
                sb.click('button:contains("Next")')
                time.sleep(10)
                successfull_signin = True
            
            #=============================
            #   Open and run notebook
            #=============================
            # - Open link
            sb.open("https://colab.research.google.com/drive/1AGqjIuFsRaxJyaQp3bETe0K7878yUczh#scrollTo=olW3XmJbcgXD") #mr0_FID_notebook #sb.open("https://colab.research.google.com/drive/1_06h399DBZOfzfVnjMo7BfaApMlwqaGD#scrollTo=WfnIjWSdVJgU") #Test_notebook
            time.sleep(10)
            
            # - Run all cells
            sb.click("body")
            sb.send_keys("body", Keys.CONTROL + Keys.F9)
            print("Run all cells: Pressed CTRL+F9 already")
            
            # - Wait for all cells to run
            wait = WebDriverWait(sb, 120)

            def find_md_icon_text():
                colab_connect_button = sb.find_element(By.CSS_SELECTOR, "colab-connect-button")

                # Use JavaScript to fetch the 'md-icon' element's text content
                interval = 1
                number_checks = 50

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

                return md_icon_text  

            def is_notebook_busy():
                
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

                    
            while not is_notebook_busy():
                print("Not found")
                time.sleep(5)  # Wait for a few seconds before checking again
            print("All cells ran")
            
            
            #=============================
            #   Save in Google drive
            #=============================
            sb.send_keys("body", Keys.CONTROL + "s")
            print("Save notebook: Pressed CTRL+S already")
            time.sleep(10)
            
            #=============================
            #   Download notebook
            #=============================
            #sb.send_keys("body", Keys.CONTROL + "a")
            #print("Download notebook: Pressed CTRL+A already")
            #time.sleep(20)
            
            #=============================
            #   Save in Github
            #=============================

            # - Retrieve name of the notebook
            input_doc_name = "#doc-name"
            notebook_name = sb.get_value(input_doc_name)

            print("Notebook name = ", notebook_name)

            # - Actually request saving in github
            sb.send_keys("body", Keys.CONTROL + "e")
            print("Saving in github: Pressed CTRL+E already")

            # - Choose correct repository
            sb.click('md-filled-select')
            sb.click('md-select-option:contains("playground-mr0/notebooks")')

            # - Provide the file path
            file_path = "results/" + notebook_name
            shadow_host = WebDriverWait(sb, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "md-outlined-text-field.github-path-input"))
            )
            shadow_root = sb.execute_script("return arguments[0].shadowRoot", shadow_host)
            input_field = shadow_root.find_element(By.CSS_SELECTOR, "div.input-wrapper > input")
            sb.execute_script("""
                const inputField = arguments[0];
                const newValue = arguments[1];
                inputField.value = newValue;
                inputField.dispatchEvent(new Event('input', { bubbles: true }));
                inputField.dispatchEvent(new Event('change', { bubbles: true }));
            """, input_field, file_path)

            # - Provide commit message
            commit_message = "hello this is my commit message"
            shadow_host2 = WebDriverWait(sb, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/mwc-dialog/div/md-outlined-text-field[2]"))
            )
            outer_shadow_root = sb.execute_script("return arguments[0].shadowRoot", shadow_host2)
            input_field = outer_shadow_root.find_element(By.CSS_SELECTOR, "span > md-outlined-field > textarea")
            sb.execute_script("""
                const inputField = arguments[0];
                const newValue = arguments[1];
                inputField.value = newValue;
                inputField.dispatchEvent(new Event('input', { bubbles: true }));
                inputField.dispatchEvent(new Event('change', { bubbles: true }));
            """, input_field, commit_message)

            # - Click OK button
            shadow_host3 = WebDriverWait(sb, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/mwc-dialog/md-text-button[2]"))
            )
            shadow_root3 = sb.execute_script("return arguments[0].shadowRoot", shadow_host3)
            ok_button = shadow_root3.find_element(By.CSS_SELECTOR, "#button")
            ok_button.click()
            
            print("End of commands")

            done_running = True
        except:
            print("Run #", run_counter, " ended abruptly...")
            done_running = False
            run_counter = run_counter + 1

    print("Exited run loop - run #", run_counter, " ended successfully")
    #while True:
    #    pass
    
