from selenium import webdriver
import os
import time
import glob

def latest_download_file():
      path = os.path.dirname(os.path.abspath(__file__)) + "\\RedditDownload"
      os.chdir(path)
      files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
      newest = files[-1]

      return newest

def autoDownloadFile(clip):
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : os.path.dirname(os.path.realpath(__file__)) + "\\RedditDownload"}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.realpath(__file__)) + "\\chromedriver.exe", chrome_options=chrome_options)

    driver.get(clip)
    try:
        time.sleep(2)
        checkIfExists = driver.execute_script('return document.querySelector(`[alt="Not like this... not like this"]`)["alt"]')
    except Exception:
        checkIfExists = None
        pass

    if checkIfExists == None:
        time.sleep(2)
        dlLink = driver.execute_script('return document.querySelector(`video`)["src"]')
        
        driver.get(dlLink)

        fileends = "crdownload"
        while "crdownload" == fileends:
            time.sleep(1)
            newest_file = latest_download_file()
            if "crdownload" in newest_file:
                fileends = "crdownload"
            else:
                fileends = "none"
                list_of_files = glob.glob(os.path.dirname(os.path.realpath(__file__)) + "\\RedditDownload\\*") # * means all if need specific format then *.csv
                latest_file = max(list_of_files, key=os.path.getctime)
                driver.close()
                return latest_file
    else:
        driver.close()
        return None

    