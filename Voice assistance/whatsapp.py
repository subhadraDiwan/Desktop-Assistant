import pyautogui
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from alexaGui import get_phone_number, speak

# create a speech recognition object
r = sr.Recognizer()

# initialize the web driver
driver = webdriver.Chrome()

# define a function to open WhatsApp Web in a new tab
def open_whatsapp():
    driver.execute_script("window.open('https://web.whatsapp.com/')")
    driver.switch_to.window(driver.window_handles[-1])

# define a function to close the current tab
def close_tab():
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()

# define a function to send a message to a given phone number
def send_message():
    recognizer = sr.Recognizer()
    
    # Prompt the user to speak the contact name
    with sr.Microphone() as source:
        print("Please speak the contact name:")
        speak("Please speak the contact name:")
        audio = recognizer.listen(source)
        
    try:
        # Recognize speech using Google Speech Recognition
        name = recognizer.recognize_google(audio)
        print("You said: " + name)

        # Get the phone number from the contact name
        phone_number = get_phone_number(name)

        if phone_number:
            print(f"Phone number found: {phone_number}")

            # Navigate to the chat search box and enter the phone number
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
            search_box.send_keys(phone_number + Keys.ENTER)

            # Wait for the chat to load
            time.sleep(2)

            # Prompt the user to speak the message
            with sr.Microphone() as source:
                print("Please speak the message:")
                audio = recognizer.listen(source)
                query = query.replace("search bar", "")
                pyautogui.hotkey('alt', 'd')
                pyautogui.write(f"{query}", 0.1)
                pyautogui.press('enter')

            # Recognize speech using Google Speech Recognition
            message = recognizer.recognize_google(audio)
            print("You said: " + message)

            # Locate the message box and enter the message
            message_box = driver.find_elements_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
            if message_box:
                message_box[0].send_keys(message)
                send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
                send_button.click()
                print(f"Message sent: {message}")
            else:
                print("Message box not found.")

    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


# loop to continuously listen for voice commands
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        try:
            # recognize speech using Google Speech Recognition
            command = r.recognize_google(audio).lower()
            print("You said: " + command)

            # execute the appropriate action based on the voice command
            if 'open whatsapp' in command:
                open_whatsapp()
            elif 'send message' in command:
                send_message()
            elif 'close tab' in command:
                close_tab()
            elif 'stop' in command:
                break
            else:
                print("Sorry, I didn't understand that.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))