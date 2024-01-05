from distutils.command import build
from email import encoders
from email.mime.base import MIMEBase
import smtplib
import typing
import openai
from alexaUi import Ui_AlexaUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject, QTimer, QTime, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
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
from typing import KeysView
import phonenumbers
import pyautogui
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
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import webbrowser
import openai
import random
from openai import Completion

import openai
from config import openai
import pyttsx3




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


CLIENT_SECRET_FILE = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'
SCOPES = ['https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox']


chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "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"
    chatStr += f"Shubha: {query}\n Alexa: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
  
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

       
# Function to get voice input from the user
def get_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = sr.recognizer.listen(source)
        try:
            text = sr.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ''
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return ''

# Function to generate a response from ChatGPT
def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Function to convert text to speech
def convert_text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def open_gmail():
    url = "https://mail.google.com/"
    webbrowser.open(url)
   

def send_mail():
    recognizer = sr.Recognizer()
    # Prompt the user to speak the email ID
    with sr.Microphone() as source:
        print("Please say the email ID:")
        speak("Please say the email ID:")
        audio = recognizer.listen(source)
    try:
        # Recognize speech using Google Speech Recognition
        email_id = recognizer.recognize_google(audio)
        print("You said: " + email_id)

        # Get the email credentials
        sender_email = 'your_email@gmail.com'  # Replace with your Gmail email address
        password = 'your_password'  # Replace with your Gmail password

        # Prompt the user to speak the subject
        with sr.Microphone() as source:
            print("Please say the subject:")
            speak("Please say the subject:")
            audio = recognizer.listen(source)

        # Recognize speech using Google Speech Recognition
        subject = recognizer.recognize_google(audio)
        print("You said: " + subject)

        # Prompt the user for attachment confirmation
        attachment_confirmation = None
        while attachment_confirmation is None:
            with sr.Microphone() as source:
                print("Do you want to attach a document? Say 'yes' or 'no'")
                speak("Do you want to attach a document? Say 'yes' or 'no'")
                audio = recognizer.listen(source)

            # Recognize speech using Google Speech Recognition
            attachment_response = recognizer.recognize_google(audio).lower()
            print("You said: " + attachment_response)

            if 'yes' in attachment_response:
                attachment_confirmation = True
                # Prompt the user to speak the document path
                with sr.Microphone() as source:
                    print("Please say the document path:")
                    speak("Please say the document path:")
                    audio = recognizer.listen(source)

                # Recognize speech using Google Speech Recognition
                document_path = recognizer.recognize_google(audio)
                print("You said: " + document_path)
                # Perform the necessary operations with the document path
                # For example, you can attach the document to the email

                # Compose the email
                message = 'This is a test email sent from Python.'

                # Connect to the SMTP server
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)

                # Send the email with attachment
                # Replace <path_to_document> with the actual path to the document
                with open(document_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment', filename='<document_filename>')
                    message.attach(part)

                server.sendmail(sender_email, email_id, message.as_string())
                print("Email with attachment sent successfully!")

                # Disconnect from the SMTP server
                server.quit()

            elif 'no' in attachment_response:
                attachment_confirmation = False
                # Compose the email without attachment

                # Connect to the SMTP server
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)

                # Send the email without attachment
                server.sendmail(sender_email, email_id, f'Subject: {subject}\n\n{message}')
                print("Email without attachment sent successfully!")

                # Disconnect from the SMTP server
                server.quit()

            else:
                print("Invalid response. Please say 'yes'")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))



def open_whatsapp():
    webbrowser.open('https://web.whatsapp.com/')
    
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
    
    
r = sr.Recognizer()

# Function to create a new file
def create_file(filename):
    try:
        with open(filename, 'w') as file:
            pass
        print("File created:", filename)
        speak("File created")
    except Exception as e:
        print("Error creating file:", e)
        speak("Error creating file")

# Function to listen to voice commands
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        recognized_text = r.recognize_google(audio)
        print("You said:", recognized_text)
        
        # Prompt user for the desired address on the desktop
        print("Please provide the desired address on the desktop:")
        speak("Please provide the desired address on the desktop")
        address = input()
        
        # Create the filename using the address and recognized text
        desktop_path = os.path.expanduser("~/Desktop")
        address = address.replace("\\", os.path.sep)  # Replace backslashes with the appropriate separator
        filename = os.path.join(desktop_path, address, recognized_text)
        create_file(filename)
        
    except sr.UnknownValueError:
        print("Could not understand audio.")
        speak("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
 
# Function to open a file
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            # Perform actions with the opened file
            # For example, you can read the contents of the file or perform any other desired operations
            file_contents = file.read()
            print("File contents:")
            print(file_contents)
            
        speak("File opened")
    except Exception as e:
        print("Error opening file:", e)
        speak("Error opening file")



# Function to listen to voice commands
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        recognized_text = r.recognize_google(audio)
        print("You said:", recognized_text)
        
        # Prompt user for the desired file name
        print("Please provide the name of the file you want to open:")
        speak("Please provide the name of the file you want to open")
        filename = input()
        
        # Open the file using the provided filename
        open_file(filename)
    except sr.UnknownValueError:
        print("Could not understand audio.")
        speak("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
 
 
 

def songs():
    return songs

def music_dir():
    return music_dir


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
        return query
    except Exception as e:
        print(e)   
        print("Say that again please.") 
        return "None"
   
    

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.Task_Gui()

    def takecommand(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source) 
            try:
                print("Recognizing...")   
                self.query = r.recognize_google(audio, language ='en-in')
                print(f"User said: {self.query}\n")
                
            except Exception as e:
                print(e)   
                print("Say that again please.") 
                return "None"
            self.query = self.query.lower()
            return self.query

    def Task_Gui(self):
        wishMe()
        speak("What can I do for You")
        while True:
            
            self.query = self.takecommand()
            
            if 'wikipedia' in self.query:
                    speak('Searching Wikipedia...')
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences = 3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                
            elif 'open chrome' in self.query:
                os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
                    
            elif 'open whatsapp' in self.query:
                open_whatsapp()
            elif 'send message' in self.query:
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
                            self.query = self.query.replace("search bar", "")
                            pyautogui.hotkey('alt', 'd')
                            pyautogui.write(f"{self.query}", 0.1)
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

            elif 'close tab' in self.query:
                close_tab()
            
            
            elif 'maximize this window' in self.query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('x')
            elif 'google search' in self.query:
                self.query = self.query.replace("google search", "")
                pyautogui.hotkey('alt', 'd')
                pyautogui.write(f"{self.query}", 0.1)
                pyautogui.press('enter')
            elif 'youtube search' in self.query:
                self.query = self.query.replace("youtube search", "")
                pyautogui.hotkey('alt', 'd')
                time.sleep(1)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.write(f"{self.query}", 0.1)
                pyautogui.press('enter')
                
            elif 'open youtube' in self.query:
                speak("what you will like to watch ?")
                self.query = takecommand().lower()
                kit.playonyt(f"{self.query}")

            elif 'close youtube' in self.query:
                os.system("taskkill /f /im msedge.exe")       
                
            elif 'open new window' in self.query:
                pyautogui.hotkey('ctrl', 'n')
                
            elif 'open incognito window' in self.query:
                pyautogui.hotkey('ctrl', 'shift', 'n')
                
            elif 'minimise this window' in self.query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('n')
                
            elif 'open history' in self.query:
                pyautogui.hotkey('ctrl', 'h')
                
            elif 'open downloads' in self.query:
                pyautogui.hotkey('ctrl', 'j')
                
            elif 'previous tab' in self.query:
                pyautogui.hotkey('ctrl', 'shift', 'tab')
                
            elif 'next tab' in self.query:
                pyautogui.hotkey('ctrl', 'tab')
                
            elif 'close tab' in self.query:
                pyautogui.hotkey('ctrl', 'w')
                
            elif 'close window' in self.query:
                pyautogui.hotkey('ctrl', 'shift', 'w')
                
            elif 'clear browsing history' in self.query:                  
                pyautogui.hotkey('ctrl', 'shift', 'delete')
                
            elif 'close chrome' in self.query:
                    os.system("taskkill /f /im chrome.exe")

            elif 'open youtube' in self.query:
                speak("Here you go to Youtube\n")
                webbrowser.open("https://www.youtube.com/")
                
            elif 'open stackoverflow' in self.query:
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

            elif "the time" in self.query:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"the time is {strTime}")
                            
            elif "open file" in self.query:
                speak("Sure! Which file would you like to open?")
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.listen(source)

                    file_name = r.recognize_google(audio)
                    speak(f"Opening {file_name}...")
                    openfile.openfile(file_name)  # Pass the file name to the openfile function

                except sr.UnknownValueError:
                    speak("Sorry, I couldn't understand the file name.")
                except sr.RequestError:
                    speak("Sorry, I'm having trouble accessing the speech recognition service.")
                except Exception as e:
                    speak("Sorry, I encountered an error while opening the file.")
                    print(e)
                    
            elif "create_file" in self.query:
                listen_command()  
                 
            elif "Open VS code" in self.query:
                codePath ="C:\\Users\\shubha\\.vscode"
                speak("Opening the visual code" )
                        
            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                    
           
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
                speak("I was created as a project by Miss shubha")
                    

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
            
            elif "create file" in self.query:
                listen_command()
            
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
                
            elif 'using Alexa' in self.query:
                 while True:
                    # Get voice input from the user
                    user_input = get_voice_input()

                    # Generate a response using ChatGPT
                    response = get_chatgpt_response(user_input)

                    # Convert the response to voice
                    convert_text_to_speech(response)

                    # Print the response to the console
                    print(response)
                    
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
                    
                 
            elif 'open Gmail' in self.query:
                speak("gmail is opening")
                print("Opening Gmail...")
                open_gmail()
            
            elif "Using AI".lower() in self.query.lower():
                ai(prompt=self.query)
                        
            elif "Alexa Quit".lower() in self.query.lower():
                exit()
                
            elif "reset chat".lower() in self.query.lower():
                chat(self.query)    
                 
            elif 'send mail' in self.query:
                recognizer = sr.Recognizer()
                # Prompt the user to speak the email ID
                with sr.Microphone() as source:
                    print("Please say the email ID:")
                    speak("Please say the email ID:")
                    audio = recognizer.listen(source)
                try:
                    # Recognize speech using Google Speech Recognition
                    email_id = recognizer.recognize_google(audio)
                    print("You said: " + email_id)

                    # Get the email credentials
                    sender_email = 'your_email@gmail.com'  # Replace with your Gmail email address
                    password = 'your_password'  # Replace with your Gmail password

                    # Prompt the user to speak the subject
                    with sr.Microphone() as source:
                        print("Please say the subject:")
                        speak("Please say the subject:")
                        audio = recognizer.listen(source)

                    # Recognize speech using Google Speech Recognition
                    subject = recognizer.recognize_google(audio)
                    print("You said: " + subject)

                    # Prompt the user for attachment confirmation
                    attachment_confirmation = None
                    while attachment_confirmation is None:
                        with sr.Microphone() as source:
                            print("Do you want to attach a document? Say 'yes' or 'no'")
                            speak("Do you want to attach a document? Say 'yes' or 'no'")
                            audio = recognizer.listen(source)

                        # Recognize speech using Google Speech Recognition
                        attachment_response = recognizer.recognize_google(audio).lower()
                        print("You said: " + attachment_response)

                        if 'yes' in attachment_response:
                            attachment_confirmation = True
                            # Prompt the user to speak the document path
                            with sr.Microphone() as source:
                                print("Please say the document path:")
                                speak("Please say the document path:")
                                audio = recognizer.listen(source)

                            # Recognize speech using Google Speech Recognition
                            document_path = recognizer.recognize_google(audio)
                            print("You said: " + document_path)
                            # Perform the necessary operations with the document path
                            # For example, you can attach the document to the email

                            # Compose the email
                            message = 'This is a test email sent from Python.'

                            # Connect to the SMTP server
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login(sender_email, password)

                            # Send the email with attachment
                            # Replace <path_to_document> with the actual path to the document
                            with open(document_path, 'rb') as attachment:
                                part = MIMEBase('application', 'octet-stream')
                                part.set_payload(attachment.read())
                                encoders.encode_base64(part)
                                part.add_header('Content-Disposition', 'attachment', filename='<document_filename>')
                                message.attach(part)

                            server.sendmail(sender_email, email_id, message.as_string())
                            print("Email with attachment sent successfully!")

                            # Disconnect from the SMTP server
                            server.quit()

                        elif 'no' in attachment_response:
                            attachment_confirmation = False
                            # Compose the email without attachment

                            # Connect to the SMTP server
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login(sender_email, password)

                            # Send the email without attachment
                            server.sendmail(sender_email, email_id, f'Subject: {subject}\n\n{message}')
                            print("Email without attachment sent successfully!")

                            # Disconnect from the SMTP server
                            server.quit()
        
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))

               
                
                          

startFunction = MainThread()        

class Gui_Start(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.alexaUi = Ui_AlexaUi()
        self.alexaUi.setupUi(self)
        
        self.alexaUi.pushButton.clicked.connect(self.startFunc)
        self.alexaUi.pushButton_2.clicked.connect(self.close)
        
    def startFunc(self):            
        
        self.alexaUi.movies_3 = QtGui.QMovie("new/giphy.gif")
        self.alexaUi.label_3.setMovie(self.alexaUi.movies_3)
        self.alexaUi.movies_3.start()
        
        startFunction.start()  
        
Gui_App = QApplication(sys.argv)
Gui_Alexa = Gui_Start()
Gui_Alexa.show()
exit(Gui_App.exec_())
              