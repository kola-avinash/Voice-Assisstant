import webbrowser
import pyjokes
import re
import smtplib
import numpy
import requests
import pyautogui
import time
# import json
import wikipedia
import os
from covid import Covid
import instaloader
from PyQt5 import QtCore, QtGui, QtWidgets
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

class Ui_AVA(object):


    def setupUi(self, AVA):
        AVA.setObjectName("AVA")
        AVA.resize(810, 577)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("AVAicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AVA.setWindowIcon(icon)
        AVA.setStyleSheet("QDialog{border-image: url(D:/voice assistant/AVAbackground.png);}")
        self.verticalLayout = QtWidgets.QVBoxLayout(AVA)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.output = QtWidgets.QLineEdit(AVA)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.output.setFont(font)
        self.output.setAutoFillBackground(False)
        self.output.setStyleSheet("color: rgb(85, 255, 0);background-color: rgb(0, 0, 0);")
        self.output.setText("")
        self.output.setFrame(True)
        self.output.setClearButtonEnabled(False)
        self.output.setObjectName("output")
        self.horizontalLayout_3.addWidget(self.output)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.start = QtWidgets.QPushButton(AVA)
        self.start.clicked.connect(self.executestart)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.start.setMouseTracking(False)
        self.start.setFocusPolicy(QtCore.Qt.NoFocus)
        self.start.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba("
                                 "0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, "
                                 "147));\n "
        "")
        self.start.setFlat(False)
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        self.pushButton = QtWidgets.QPushButton(AVA)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, "
                                      "fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, "
                                      "147), stop:1 rgba(0, 169, 255, 147));\n "
                                        "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.input = QtWidgets.QLineEdit(AVA)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input.setFont(font)
        self.input.setAutoFillBackground(False)
        self.input.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(85, 255, 0);")
        self.input.setFrame(True)
        self.input.setObjectName("input")
        self.horizontalLayout_2.addWidget(self.input)
        self.send = QtWidgets.QPushButton(AVA)
        self.send.clicked.connect(self.execute)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, "
                                "fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), "
                                "stop:1 rgba(0, 169, 255, 147));\n "
                                "color: rgb(255, 255, 255);")
        self.send.setFlat(False)
        self.send.setObjectName("send")
        self.horizontalLayout_2.addWidget(self.send)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(AVA)
        QtCore.QMetaObject.connectSlotsByName(AVA)

    def retranslateUi(self, AVA):
        _translate = QtCore.QCoreApplication.translate
        AVA.setWindowTitle(_translate("AVA", "AVA Assiatant"))
        self.start.setText(_translate("AVA", "START"))
        self.pushButton.setText(_translate("AVA", "STOP"))
        self.send.setText(_translate("AVA", "SEND"))

    # def printf(self):
    #     self.output.setText("avinash")

    def talk(self, audio):
        engine.setProperty('rate', 175)
        engine.say(audio)
        engine.runAndWait()

    def recognise(self):
        r = sr.Recognizer()
        r.energy_threshold = 5000
        with sr.Microphone() as source:
            self.output.setText("listening....")
            audio = r.listen(source)

        try:
            self.output.setText("recognizing..")
            query = str(r.recognize_google(audio))
            query = query.lower()
            self.output.setText(query)

        except Exception as e:
            print(e)
            # self.talk("can you say that again")
            return "none"
        return query

    def optimize(self, query):
        stopwords = ['for', 'in', 'what', 'is', 'that', 'google', 'search', 'youtube', 'amazon', 'meant', 'do', 'by',
                     'you'
            , 'mean', 'can', 'please', 'open', 'and']
        command = query
        resultwords = [word for word in command.split() if word.lower() not in stopwords]
        command = ' '.join(resultwords)
        return command

    def search(self, query):
        if 'google' in query:
            query = self.optimize(query)
            url = 'https://www.google.co.in/search?q='
            search_url = url + query

        elif 'youtube' in query:
            query = self.optimize(query)
            url = 'https://www.youtube.com/results?search_query='
            search_url = url + query

        elif 'amazon' in query:
            query = self.optimize(query)
            url = 'https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='
            search_url = url + query

        elif 'wikipedia' in query:
            self.talk('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            query = self.optimize(query)
            search_url = 'https://en.wikipedia.org/wiki/' + query
            self.talk("According to Wikipedia")
            print(results)
            self.talk(results)

        else:
            query = self.optimize(query)
            url = 'https://www.google.co.in/search?q='
            search_url = url + query

        webbrowser.open(search_url)

    def jokes(self):
        self.talk(pyjokes.get_joke())

    def gentalk(self, query):
        if 'what is your name' in query or "what's your name" in query:
            self.talk('my name is Ava')

        elif 'hai' in query or 'hello' in query:
            self.talk("hello, i am ava. how can i help you?")

        elif 'tell me about yourself' in query:
            self.talk("my name is ava and i was developed by avinash")

        elif 'how are you' in query:
            self.talk("I am fine, Thank you")
            self.talk("How are you Sir")

        elif 'fine' in query or "good" in query:
            self.talk("It's good to know that your fine")

        elif 'i love you' in query:
            self.talk("i love you too sir")

        elif 'i am bored' in query:
            self.talk("do you want me to tell you a joke")
            a = self.recognise()
            if 'yes' in a or 'ok' in a:
                self.jokes()
            else:
                self.talk('do you want me to open youtube')
                a = self.recognise()
                if 'yes' in a or 'ok' in a:
                    self.search('youtube')

        elif 'do you have feelings' in query or 'do you have emotions' in query:
            self.talk("i have lots of emotions, i feel happy when i can help you")

        elif 'do you have a girlfriend' in query:
            self.talk("No bro, i am single like you")

        elif 'what can you do' in query:
            self.talk('i can search in web anything you ask, i can also open any application')
            self.talk('and i can do many more you could think of')

        elif 'where are you' in query:
            self.talk("i am in your computer")

        elif 'what is my name' in query:
            owner = 'Avinash'
            self.talk(owner)

        elif 'thanks' in query or 'excellent' in query:
            self.talk("thank you, it is a honour to help you")

        else:
            self.search(query)

    def sendmail(self):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login("damonsalvatore2929@gmail.com", "Damon@2001")
        self.talk("would you like to add a new mail id to send or send to existing friends")
        emails = {'hemanth': 'hemanthr1711@gmail.com', 'revanth': 'saireventhalapati03@gmail.com',
                  'sushma': 'saisushmanth1919@gmail.com'
            , 'ganesh': 'ganesh.konagala.11@gmail.com', 'chandu': 'snchandu1@gmail.com', 'bhargav': 'vbrcrl@gmail.com ',
                  'avinash': 'avinashkola1999@gmail.com'}
        x = self.recognise()
        if 'add' in x:
            self.talk("enter mail id using keyboard")
            email = input()
            self.talk("what would you like to call him")
            name = input()
            emails[name] = email

        self.talk('who should i send mail')
        dest = self.recognise()
        dest = dest.replace(" ", "")
        dest = emails.get(dest)
        print(dest)
        self.talk("send mail yes or no")
        con = self.recognise()
        if 'yes' in con:
            self.talk("tell me the message to be sent")
            message = self.recognise()
            s.sendmail("damonsalvatore2929@gmail.com", dest, message)
            print('done')
            self.talk("mail sent succesfully")
            s.quit()
        else:
            self.talk('do you again want to say mail ID')
            con = self.recognise()
            if 'yes' in con:
                self.sendmail()
            else:
                exit()

    def calculate(self, query):
        if 'add' in query or 'addition' in query or 'sum' in query or 'plus' in query or '+' in query:
            numbers = re.findall('[0-9]+', query)
            numbers = list(map(int, numbers))
            print((sum(numbers)))
            self.talk(sum(numbers))
        elif 'subtract' in query or 'minus' in query or '-' in query:
            numbers = re.findall('[0-9]+', query)
            numbers = list(map(int, numbers))
            self.talk(numbers[0] - numbers[1])
        elif 'mulitplication' in query or 'multiply' in query or 'into' in query:
            numbers = re.findall('[0-9]+', query)
            numbers = list(map(int, numbers))
            print(numpy.prod(numbers))
            self.talk(numpy.prod(numbers))
        elif 'divide' in query or 'divided' in query:
            numbers = re.findall('[0-9]+', query)
            numbers = list(map(int, numbers))
            self.talk(numbers[0] / numbers[1])
        else:
            self.search(query)

    def weather(self):
        api_key = "d3c7405be8b93416a47ae7fea760a821"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.talk("tell me the city name to find weather update")
        city_name = self.recognise()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            self.talk(" Temperature is " +
                 str(current_temperature) +
                 ", atmospheric pressure  is " +
                 str(current_pressure) +
                 ", humidity is" +
                 str(current_humidiy) +
                 ", overall weather description is" +
                 str(weather_description))

        else:
            self.talk("City Not Found ")

    def screenshot(self):
        name = int(round(time.time() * 1000))
        name = 'D:/voice assistant/assistantshots/{}.png'.format(name)
        self.talk("screenshot is taken in 3 seconds")
        time.sleep(3)
        img = pyautogui.screenshot(name)
        self.talk("image shot")
        self.talk("do you want me to show the image")
        a = self.recognise()
        if 'yes' in a:
            img.show()
        else:
            exit()

    def instagram(self):
        self.talk("enter the username to download their profile picture")
        name = input()
        mod = instaloader.Instaloader()
        mod.download_profile(name, profile_pic_only=True)
        self.talk("image downloaded successfully")

    def openapp(self, query):
        if 'chrome' in query:
            self.talk("opening chrome")
            os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        elif 'firefox' in query:
            self.talk("opening mozilla firefox")
            os.startfile(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        elif 'word' in query or 'ms word' in query:
            self.talk("opening microsoft word")
            os.startfile(
                r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010.lnk")
        elif 'excel' in query:
            self.talk("opening microsoft excel sheet")
            os.startfile(
                r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Excel 2010.lnk")
        elif 'powerpoint' in query or 'ppt' in query:
            self.talk("opening microsoft powerpoint")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft PowerPoint "
                         r"2010.lnk")
        elif 'vscode' in query or 'visual studio' in query:
            self.talk("opening visual studio")
            os.startfile(r"C:\Users\Avinash\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        elif 'teams' in query or 'msteams' in query:
            self.talk("opening microsoft teams")
            os.startfile(r"C:\Users\Avinash\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams.lnk")

        elif 'steam' in query:
            self.talk("opening steam")
            os.startfile(r"D:\games\steam.exe")

        else:
            self.search(query)

    def covidupdates(self):
        covid = Covid()
        self.talk("tell the name of the country to find updates")
        name = self.recognise()
        country = covid.get_status_by_country_name(name)
        self.talk("confirmed cases are {} , active cases are {}, deaths are {}, recovered cases are {}".
             format(country.get('confirmed'), country.get('active'), country.get('deaths'), country.get('recovered')))

    def welcome(self, audio):
        # audio = self.recognise()
        googwords = ['search', 'google', 'youtube', 'amazon', 'meant', 'mean']
        calwords = ['add', 'subtract', 'divided', 'multiply', 'into', '-', '+', 'calculate', 'minus', 'plus', '/',
                    'divide']
        if 'joke' in audio:
            self.jokes()
            self.talk("that's a Right One Ha Ha Ha")

        elif any(word in audio for word in googwords):
            self.search(audio)

        elif 'mail' in audio or 'email' in audio:
            self.sendmail()

        elif any(word in audio for word in calwords):
            self.calculate(audio)

        elif 'weather' in audio:
            self.weather()

        elif 'screenshot' in audio:
            self.screenshot()

        elif 'covid' in audio or 'coronovirus' in audio:
            self.covidupdates()

        elif 'instagram' in audio:
            self.instagram()

        elif 'open' in audio:
            self.openapp(audio)

        else:
            self.gentalk(audio)

    def execute(self):
        query = self.input.text()
        self.welcome(query)

    def executestart(self):
        i = 1
        self.talk("welcome to the voice based search assistant")
        self.talk("try saying a term to search or ask me a Joke or you can open a application also")
        while i <= 10:
            query = self.recognise()
            if 'stop' in query or 'exit' in query:
                self.talk("good bye sir")
                break
            self.welcome(query)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AVA = QtWidgets.QDialog()
    ui = Ui_AVA()
    ui.setupUi(AVA)
    AVA.show()
    sys.exit(app.exec_())
