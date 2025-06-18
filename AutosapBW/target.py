# ****************************************************************************
#  Program Description : Script downloads the Lots from Target System        *
#  Program Name:  AutosapBW\target.py                                        *
#          Date:  21/06/2024                                                 *
#       version:  1.0.0                                                      *
#        Author:  Erry Lavakumar                                             *
#  Return Codes:                                                             *
#                 0 - Success                                                *
#                 1 - Error check log file                                   *
# ****************************************************************************
#  AutoSAP Automation                                                        *
#  --------------------                                                      *
#  Sr.         Role           Member          Email                          *
#  ---------   ----------     --------------  -------------------------------*
#  1           Developer      NIKHIL CHALIKWAR  nikhil.x.chalikwar@gsk.com   *
#  2           Developer      Erry Lavakumar    erry.8.lavakumar@gsk.com     *  
#  2           Developer      Akoju Sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************

# Function to Download the Lots Report from Target( JAVA PORTAL ) #
def target(path=0,daterange=0,stamp=0):
    try:
        # import selenium
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.edge.service import Service
        from msedge.selenium_tools import Edge, EdgeOptions
        import os

        download_dir = os.path.join(os.getcwd(),'excel data',f'AutoSAP_{stamp}')
        edge_options= EdgeOptions()
        edge_options.use_chromium= True
        prefs={"download.default_directory":download_dir,"download.prompt_for_download":False, "download.directory_upgrade":True, "safebrowsing.enabled":True}
        edge_options.add_argument("--disable-blink-features=AutomationControlled")
        edge_options.add_argument("--disable-extensions")
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--disable-infobars")
        edge_options.add_argument("--start-maximized")
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        edge_options.add_experimental_option("prefs",prefs)
        driver=Edge(executable_path=r"msedgedriver.exe",options=edge_options)

        driver.maximize_window()
        driver.get("https://rixsapbjt071.sbbio.be:57101/irj/servlet/prt/portal/prtroot/pcd!3aportal_content!2fcom.sap.pct!2fplatform_add_ons!2fcom.sap.ip.bi!2fiViews!2fcom.sap.ip.bi.bex?QUERY=ZRB_YGMP_Q015_1_TEST")
        uid=driver.find_element_by_xpath('//*[@id="logonuidfield"]')

        import cc
        import logon
        uid.send_keys(cc.javaid)
        pswd=driver.find_element_by_xpath('//*[@id="logonpassfield"]')
        pswd.send_keys(logon.decrypt_aes256(logon.key, cc.javapass))
        sub=driver.find_element_by_xpath('//*[@id="certLogonForm"]/table/tbody/tr[5]/td[2]/input')
        sub.send_keys(Keys.ENTER)

        newframe= WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'iframe_Roundtrip_9223372036563636042')))

        dates=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'DLG_VARIABLE_vsc_cvl_VAR_1_INPUT_inp'))) #'DLG_VARIABLE_vsc_cvl_VAR_1_INPUT_inp' DLG_VARIABLE_vsc_cvl_VAR_1_INPUT_inp-r
        dates.clear()
        dates.send_keys(daterange) 

        ok=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"DLG_VARIABLE_dlgBase_BTNOK")))
        ok.send_keys(Keys.ENTER)

        button=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "BUTTON_TOOLBAR_2_btn2_acButton")))
        button.click()

        import time
        time.sleep(1)
        
        def wait_for_download(dir,timeout=30):
            end_time=time.time()+timeout
            while time.time()<end_time:
                if any(fname.endswith('.crdownload') for fname in os.listdir(dir)):
                    time.sleep(1)
                else:
                    break

        wait_for_download(download_dir)
        driver.quit()
        print("Target File Downloaded Successfully!!")
        return 0
    except Exception as e:
        print({"Error in Selenium":e})

