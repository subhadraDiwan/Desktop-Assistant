"""
import os
import re
import sys
from winsound import PlaySound
from PyQt5.QtWidgets import QWidget
from click import BaseCommand, command
from numpy import source
#import random
from pyautogui import KEYBOARD_KEYS
import pyautogui
#import pywhatkit
import pywhatkit
import requests
import ctypes
import datetime
import json
import os
import shutil
import subprocess
import time
import webbrowser
from urllib.request import urlopen
#import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import winshell
import webbrowser
import wolframalpha
import time
import keyboard
import pywhatkit as kit
from clint.textui import progress
from ecapture import ecapture as ec
from twilio.rest import Client
from openfile import openfile
import gmail
from ask_sdk_core.dispatch_components import (AbstractRequestHandler, AbstractExceptionHandler)
from ask_sdk_core.handler_input import HandlerInput
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from googlesearch import search
import googlesearch
import phonenumbers
import time
from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from typing import KeysView, Self
import phonenumbers
import pyautogui
import speech_recognition as sr
import webbrowser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import googlesearch
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyttsx3
from phonenumbers.phonenumberutil import NumberParseException
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
     
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")
  
    else:
        speak("Good Evening!")
  
    assname =("Alexa ")
    speak("I am your Alexa")
    #speak(assname)
                                    
def open_whatsapp():
    webbrowser.open('https://web.whatsapp.com/')

def close_tab():
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()
    
def get_phone_number(name):
    query = f"{name} phone number"
    search_results = googlesearch.search(query, num_results=1)
    for result in search_results:
        if "phone" in result.lower():
            phone_str = ''.join(filter(str.isdigit, result))
            try:
                phone_number = phonenumbers.parse(phone_str, None)
                return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
            except NumberParseException:
                # Handle invalid phone number case
                return None
    return None

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
        else:
            print(f"No phone number found for contact: {name}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def play_music():
    speak("Do you want to play music from an online source or from your local device?")
    while True:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            audio = r.listen(source)
            try:
                user_input = r.recognize_google(audio)
                if "online" in user_input:
                    speak("Please say the name of the song and artist you want to play")
                    audio = r.listen(source)
                    try:
                        query = r.recognize_google(audio)
                        query = query.replace(' ', '+')
                        url = f"https://www.youtube.com/results?search_query={query}"
                        webbrowser.get().open(url)
                        return
                    except sr.UnknownValueError:
                        speak("Sorry, I didn't understand what you said.")
                    except sr.RequestError as e:
                        speak(f"Could not request results from Google Speech Recognition service; {e}")
                elif "local" in user_input:
                    speak("Here you go with music")
                    music_dir = "E:\\My Songs\\Vedio"
                    songs = os.listdir(music_dir)
                    print(songs)
                    song_index = 0
                    pygame.mixer.init()
                    pygame.mixer.music.load(os.path.join(music_dir, songs[song_index]))
                    pygame.mixer.music.play()
                    while True:
                        if keyboard.is_pressed('p'):  # pause music
                            pygame.mixer.music.pause()
                            speak("Music paused")
                            while True:
                                if keyboard.is_pressed('r'):  # resume music
                                    pygame.mixer.music.unpause()
                                    speak("Music resumed")
                                    break
                                elif keyboard.is_pressed('s'):  # stop music
                                    pygame.mixer.music.stop()
                                    speak("Music stopped")
                                    return
                                time.sleep(0.1)
                        elif keyboard.is_pressed('n'):  # play next song
                            song_index = (song_index + 1) % len(songs)
                            pygame.mixer.music.load(os.path.join(music_dir, songs[song_index]))
                            pygame.mixer.music.play()
                            speak(f"Now playing {songs[song_index]}")
                            time.sleep(0.1)
                        elif keyboard.is_pressed('s'):  # stop music
                            pygame.mixer.music.stop()
                            speak("Music stopped")
                            return
                        time.sleep(0.1)
                else:
                    speak("Sorry, I didn't understand what you said. Please try again.")
            except sr.UnknownValueError:
                speak("Sorry, I didn't understand what you said.")
            except sr.RequestError as e:
                speak(f"Could not request results from Google Speech Recognition service; {e}")

def pygame():
    pygame.mixer.init()
        
def songs():
    return songs

def music_dir():
    return music_dir


def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source) 
        try:
            print("Recognizing...")   
            query = r.recognize_google(audio, language ='en-in')
            print(f"User said: {query}\n")
            
        except Exception as e:
            print(e)   
            print("Say that again please.") 
            return "None"
        query = query.lower()
        return query


def Task_Gui():
    wishMe()
    while True:
        self.query = self.takecommand()
        
        if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
        elif 'open chrome' in self.query:
            os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
                
        elif 'open whatsapp' in query:
            open_whatsapp()
        elif 'send message' in query:
            send_message()
        elif 'close tab' in query:
            close_tab()
        

        elif 'maximize this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        elif 'youtube search' in query:
            query = query.replace("youtube search", "")
            pyautogui.hotkey('alt', 'd')
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
            
        elif 'open youtube' in query:
            speak("what you will like to watch ?")
            qrry = takecommand().lower()
            kit.playonyt(f"{qrry}")

        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")    
            
            
        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')
        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')
        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')
        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')
        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')
        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')
        elif 'clear browsing history' in query:                  
            pyautogui.hotkey('ctrl', 'shift', 'delete')
        elif 'close chrome' in query:
                os.system("taskkill /f /im chrome.exe")

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("https://www.youtube.com/")
            
            
            
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
                
            
        elif keyboard.is_pressed('r'):  # resume music
                pygame.mixer.music.unpause()
                speak("Music resumed")
                break
        elif keyboard.is_pressed('s'):  # stop music
                pygame.mixer.music.stop()
                speak("Music stopped")
                time.sleep(0.1)
        elif keyboard.is_pressed('n'):  # play next song
                song_index = (song_index + 1) % len(songs())
                pygame.mixer.music.load(os.path.join(music_dir(), songs[song_index]))
                pygame.mixer.music.play()
                speak(f"Now playing {songs[song_index]}")
                time.sleep(0.1)
        elif keyboard.is_pressed('s'):  # stop music
                pygame.mixer.music.stop()
                speak("Music stopped")
                time.sleep(0.1)

        elif "the time" in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")
                        
                    
        elif "openfile" in query:
                speak("file is opening")
                openfile.openfile()     
                    
                
        elif "Open VS code" in query:
            codePath ="C:\\Users\\shubha\\.vscode"
            speak("Opening the visual code" )
            
                
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
                

        elif "how are you" in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
                

        elif "fine" in query or "good" in query:
            speak("It's good to know that your fine")
                

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
            

        elif "change name" in self.query:
            speak("What would you like to call me")
            assname = self.takecommand()
            speak("Thanks for naming me")
            

        elif "what's your name" in self.query or "What is your name" in self.query:
            speak("My friends call me")
            speak("seriyo")
            print("My friends call me")

        elif "exit" in self.query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in self.query or "who created you" in self.query:
            speak("I have been created by shubha.")
                
                
        elif "calculate" in self.query:
            
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = self.query.lower().split().index("calculate")
            self.query = self.query.split()[indx + 1:]
            res = client.query(' '.join(self.query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "search" in self.query or 'play' in self.query:
            self.query = self.query.replace("search", " ")
            self.query = self.query.replace("play", " ")         
            webbrowser.open(self.query)

        elif "who i am" in self.query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in self.query:
            speak("Thanks to shubha. further It's a secret")

        elif "power point presentation" in self.query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif "is love" in self.query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in self.query:
            speak("I am your virtual assistant created by shubha")

        elif "reason for you" in self.query:
            speak("I was created as a Minor project by Miss shubha ")
                

        elif "change background" in self.query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                        0,
                                                        "Location of wallpaper",
                                                        0)
            speak("Background changed successfully")

        elif "open bluestack" in self.query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)
                

        elif "news" in self.query:
                
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                    
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                    
                for item in data['articles']:
                
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                    
                    print(str(e))
            
        elif "lock window" in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif "shutdown system" in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                    
        elif "empty recycle bin" in self.query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in self.query or "stop listening" in self.query:
            speak("For how many seconds do you want to stop Alexa from listening to commands?")
            a = self.takecommand()
                
            try:
                a = int(a)
                print(f"Alexa will stop listening for {a} seconds.")
                time.sleep(a)
            except ValueError:
                speak("Sorry, I did not understand the number you said. Please try again.")

        elif "where is" in self.query:
            self.query = self.query.replace("where is", "")
            location = self.query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in self.query or "take a photo" in self.query:
            ec.capture(0, "Alexa Camera ", "img.jpg")

        elif "restart" in self.query:
            subprocess.call(["shutdown", "/r"])
                
        elif "hibernate" in self.query or "sleep" in self.query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in self.query or "sign out" in self.query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
                
        elif "volume up" in self.query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
                
        elif "volume down" in self.query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            
        elif "mute" in self.query:
            pyautogui.press("volumemute")
                    
        elif "refresh" in self.query:
            pyautogui.moveTo(1551,551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620,667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
                
        elif "scroll up" in self.query:
            pyautogui.scroll(1000)
                
        elif "drag visual studio to the right" in self.query:
            pyautogui.moveTo(46, 31, 2)
            pyautogui.dragRel(1857, 31, 2)
                
        elif "rectangular spiral" in self.query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('paint')
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.moveTo(100, 193, 1)
            pyautogui.rightClick
            pyautogui.click()
            distance = 300

        elif "write a note" in self.query:
                speak("What should i write, mam")
                note = self.takecommand()
                file = open('Alexa.txt', 'w')
                speak("mam, Should i include date and time")
                snfm = self.takecommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
            
        elif "show note" in self.query:      
            speak("Showing Notes")
            file = open("dsk.txt", "r")
            print(file.read())
            speak(file.read(6))
                
        elif "weather" in self.query:
            speak(" Please tell your city name ")
            print("City name : ")
            def get_weather(api_key, location):
                weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(location, api_key)
                weather_res = requests.get(weather_url)
                weather_json = weather_res.json()
                return weather_json

            def display_weather(weather_json):
                print("Weather in {}:".format(weather_json["name"]))
                print("Temperature: {}°C".format(weather_json["main"]["temp"]))
                print("Humidity: {}%".format(weather_json["main"]["humidity"]))
                print("Pressure: {} hPa".format(weather_json["main"]["pressure"]))
                print("Weather: {}".format(weather_json["weather"][0]["description"]))
        
        elif "wikipedia" in self.query:
            webbrowser.open("wikipedia.com")
                
        elif "VsCode" in self.query:
            os.startfile("C:\\Users\\shubh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code")
        
        elif "Telegram" in self.query:
            os.startfile("C:\\Users\\shubh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Telegram Desktop")
        
        elif "pycham" in self.query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains")
        
        elif "andriodStudio" in self.query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio")
        
        elif "Instagram" in self.query:
            webbrowser.open('https://www.instagram.com/')
        
        elif "map" in self.query:
            webbrowser.open("https://www.google.com/maps")

        elif "how are you" in self.query:
            speak("I'm fine, glad you me that")
                
        elif "open Whatsapp" in self.query:
                # loop to continuously listen for voice commands
                    

                # function to send a message to a contact
                def send_message():
                    # prompt the user to speak the contact name
                    with sr.Microphone() as source:
                        print("Please speak the contact name:")
                        speak("Please speak the contact name")
                        audio = re.listen(source)

                    try:
                        # recognize speech using Google Speech Recognition
                        name = re.recognize_google(audio)
                        print("You said: " + name)

                        # get the phone number from the contact name
                        phone_number = get_phone_number(name)

                        if phone_number:
                            print(f"Phone number found: {phone_number}")
                            # navigate to the chat search box and enter the phone number
                            search_box = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
                            search_box.send_keys(phone_number + Keys.ENTER)

                            # wait for the chat to load
                            time.sleep(2)

                            # prompt the user to speak the message
                            with sr.Microphone() as source:
                                print("Please speak the message:")
                                speak("Please speak the message")
                                audio = re.listen(source)

                            # recognize speech using Google Speech Recognition
                            message = re.recognize_google(audio)
                            print("You said: " + message)

                            # locate the message box and enter the message
                            message_box = driver.find_elements_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
                            if message_box:
                                message_box[0].send_keys(message)
                                send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
                                send_button.click()
                                print(f"Message sent: {message}")
                            else:
                                print("Message box not found.")
                                speak("Message box not found")
                        else:
                            print(f"No phone number found for contact: {name}")
                            speak("No phone number found for contact")
                    except sr.UnknownValueError:
                        print("Sorry, I could not understand audio.")
                        speak("Sorry, I could not understand audio")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))

                # call the send_message function
                send_message()

        elif "open Gmail" in self.query:
            speak("Gmail is open")
            print("Gmail is opening")
            gmail.mygmail()
                        
    

        elif "what is" in self.query or "who is" in self.query:
            
                # Use the same API key
                # that we have generated earlier
                client = wolframalpha.Client("API_ID")
                res = client.query(self.query)
                
                try:
                    print (next(res.results).text)
                    speak (next(res.results).text)
                except StopIteration:
                    print ("No results")

"""