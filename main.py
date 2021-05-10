import time
from datetime import datetime
from plyer import notification
import pandas as pd
from selenium import webdriver
import pyautogui
#meeting id input box id =btnSubmit
# join button class id = _1FvRrPS6

def join_meeting(id,passcode):
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get('https://zoom.us/join')
    join_box = chrome.find_element_by_id('join-confno')
    joinbtn=chrome.find_element_by_id('btnSubmit')
    join_box.clear()
    join_box.send_keys(id)
    joinbtn.click()
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.write(passcode)
    pyautogui.press("enter")
    notification.notify(
        title='good things take time',
        message=f"still joining your zoom meeting..",
        timeout=3)
    time.sleep(10)

    pyautogui.press("esc")
    pyautogui.press("esc")
    pyautogui.press("esc")
    notification.notify(
        title='you nailed it',
        message=f"joined zoom successfully",
        timeout=4)
    time.sleep(100)
meetingdetails= pd.read_csv('timings.csv')
while True:
    now = datetime.now().strftime("%H:%M%p")
    if now in str(meetingdetails['timings']):

       row = meetingdetails.loc[meetingdetails['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])
       m_name=str(row.iloc[0,3])
       notification.notify(
           title='zoom auto join',
           message=f"joining {m_name}, make sure to have good internet",
           timeout=3)

       join_meeting(m_id, m_pswd)

