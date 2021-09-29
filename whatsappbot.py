
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

import time
import speech_recognition
import pyttsx3
import wikipedia as wikipedia


class Assitant :
    def __init__(self):
        '''
        we will set our engine to Pyttsx3 which is used for text to speech in Python and
        sapi5 is Microsoft speech application platform interface we will be using this for text to speech function.
        '''

        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')

        self.engine.setProperty('voice',voices[0].id) # You can change voice Id to “0” for Male voice

    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def takecommand(self):

        recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
            print('Listening ....')
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "sorry"

        return query

    def wishMe(self):
        hour = int(datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak("Good Morning Sir !")

        elif hour >= 12 and hour < 18:
            self.speak("Good Afternoon Sir !")

        else:
            self.speak("Good Evening Sir !")

        ass_name = ("DCIKIGAI private limited")
        self.speak("I am your Assistant")
        self.speak(ass_name)

    def whatsapp(self):


        # Replace below path with the absolute path
        path = r'C:\Users\PAWAN\Desktop\driver\chromedriver.exe'

        # to chromedriver in your computer
        driver = webdriver.Chrome(path)

        driver.get("https://web.whatsapp.com/")
        wait = WebDriverWait(driver, 900)
        time.sleep(20)

        country_code = input('Enter country code :   \n')
        name = input('Enter person''s name or number: \n')
        search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        search.send_keys(country_code + name)
        search.send_keys(Keys.ENTER)
        msg = int(input('Enter your choice : \n1. Text message \n2. Voice message'))
        if msg == 2:
            message = self.takecommand()
        else:
            message = input('enter message : ')

        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')

        for i in range(1):
            msg_box.send_keys(message)
            button = driver.find_element_by_class_name('_4sWnG')
            button.click()
            time.sleep(1)


if __name__ == '__main__':
    ass = Assitant()
    ass.wishMe()

    ass.whatsapp()


# In[ ]:




