import pyttsx3
import speech_recognition as sr
import webbrowser
import pyjokes
import re
import smtplib
import numpy
import requests
import pyautogui
import time
import json

engine = pyttsx3.init()
stopcode = 0

def talk(audio):
    engine.setProperty('rate', 175)
    engine.say(audio)
    engine.runAndWait()


def recognise():
    r = sr.Recognizer()
    r.energy_threshold = 5000
    with sr.Microphone() as source:
        print("listening....")
        audio = r.listen(source)

    try:
        print("recognizing..")
        query = str(r.recognize_google(audio))
        query = query.lower()
        print(query)

    except Exception as e:
        print(e)
        talk("can you say that again")
        return "none"
    return query


def optimize(query):
    stopwords = ['for', 'in', 'what', 'is', 'that', 'google', 'search', 'youtube', 'amazon', 'meant', 'do', 'by', 'you'
                        , 'mean', 'can', 'please', 'open', 'and']
    command = query
    resultwords = [word for word in command.split() if word.lower() not in stopwords]
    command = ' '.join(resultwords)
    return command


def search(query):
    if 'google' in query:
        query = optimize(query)
        url = 'https://www.google.co.in/search?q='
        search_url = url + query

    elif 'youtube' in query:
        query = optimize(query)
        url = 'https://www.youtube.com/results?search_query='
        search_url = url + query

    elif 'amazon' in query:
        query = optimize(query)
        url = 'https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='
        search_url = url + query

    else:
        query = optimize(query)
        url = 'https://www.google.co.in/search?q='
        search_url = url + query

    webbrowser.open(search_url)


def jokes():
    talk(pyjokes.get_joke())


def gentalk(query):
    if 'what is your name' in query or "what's your name" in query:
        talk('my name is Ava')

    elif 'hai' in query or 'hello' in query:
        talk("hello, i am ava. how can i help you?")

    elif 'tell me about yourself' in query:
        talk("my name is ava and i was developed by avinash")

    elif 'how are you' in query:
        talk("I am fine, Thank you")
        talk("How are you Sir")

    elif 'fine' in query or "good" in query:
        talk("It's good to know that your fine")

    elif 'i love you' in query:
        talk("i love you too sir")

    elif 'i am bored' in query:
        talk("do you want me to tell you a joke")
        a = recognise()
        if 'yes' in a or 'ok' in a:
            jokes()
        else:
            talk('do you want me to open youtube')
            a = recognise()
            if 'yes' in a or 'ok' in a:
                search('youtube')

    elif 'do you have feelings' in query or 'do you have emotions' in query:
        talk("i have lots of emotions, i feel happy when i can help you")

    elif 'do you have girlfriend' in query:
        talk("No bro, i am single like you")

    elif 'what can you do' in query:
        talk('i can search in web anything you ask, i can also open any application')
        talk('and i can do many more you could think of')

    elif 'where are you' in query:
        talk("i am in your computer")

    elif 'what is my name' in query:
        owner = 'Avinash'
        talk(owner)

    elif 'thanks' in query or 'excellent' in query:
        talk("thank you, it is a honour to help you")

    else:
        talk("sorry i didn't catch that")


def sendmail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login("damonsalvatore2929@gmail.com", "Damon@2001")
    talk("would you like to add a new mail id to send or send to existing friends")
    emails={'hemanth':'hemanthr1711@gmail.com', 'revanth': 'saireventhalapati03@gmail.com', 'sushma': 'saisushmanth1919@gmail.com'
            , 'ganesh':'ganesh.konagala.11@gmail.com', 'chandu': 'snchandu1@gmail.com', 'bhargav': 'vbrcrl@gmail.com ','avinash': 'avinashkola1999@gmail.com'}
    x = recognise()
    if 'add' in x:
        talk("enter mail id using keyboard")
        email=input()
        talk("what would you like to call him")
        name=input()
        emails[name] = email

    talk('who should i send mail')
    dest = recognise()
    dest = dest.replace(" ", "")
    dest = emails.get(dest)
    print(dest)
    talk("send mail yes or no")
    con = recognise()
    if 'yes' in con:
        talk("tell me the message to be sent")
        message = recognise()
        s.sendmail("damonsalvatore2929@gmail.com", dest, message)
        print('done')
        talk("mail sent succesfully")
        s.quit()
        exit()
    else:
        talk('do you again want to say mail ID')
        con = recognise()
        if 'yes' in con:
            sendmail()
        else:
            exit()


def calculate(query):
    if 'add' in query or 'addition' in query or 'sum' in query or 'plus' in query:
        numbers = re.findall('[0-9]+', query)
        numbers = list(map(int, numbers))
        talk(sum(numbers))
    elif 'subtract' in query or 'minus' in query or '-' in query:
        numbers = re.findall('[0-9]+', query)
        numbers = list(map(int, numbers))
        talk(numbers[0]-numbers[1])
    elif 'mulitplication' in query or 'multiply' in query or 'into' in query:
        numbers = re.findall('[0-9]+', query)
        numbers = list(map(int, numbers))
        talk(numpy.prod(numbers))
    elif 'divide' in query or 'divided' in query:
        numbers = re.findall('[0-9]+', query)
        numbers = list(map(int, numbers))
        talk(numbers[0]/numbers[1])
    else:
        search(query)


def weather():
    api_key = "d3c7405be8b93416a47ae7fea760a821"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    talk("tell me the city name to find weather update")
    city_name = recognise()
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
        talk(" Temperature is " +
              str(current_temperature) +
              ", atmospheric pressure  is " +
              str(current_pressure) +
              ", humidity is" +
              str(current_humidiy) +
              ", overall weather description is" +
              str(weather_description))

    else:
        talk("City Not Found ")


def screenshot():
    name = int(round(time.time()*1000))
    name = 'D:/voice assistant/assistantshots/{}.png'.format(name)
    talk("screenshot is taken in 3 seconds")
    time.sleep(3)
    img = pyautogui.screenshot(name)
    talk("image shot")
    talk("do you want me to show the image")
    a = recognise()
    if 'yes' in a:
        img.show()
        exit()
    else:
        exit()


def welcome():
    #talk("welcome to the voice based search assistant")
    #talk("try saying a term to search or ask me a Joke or you can open a application also")
    audio = recognise()
    googwords = ['search', 'google', 'youtube', 'amazon', 'meant', 'mean']
    calwords = ['add', 'subtract', 'divided', 'multiply', 'into', '-', '+', 'calculate', 'minus', 'plus', '/', 'divide']
    if 'joke' in audio:
        jokes()
        talk("that's a Right One Ha Ha Ha")

    elif any(word in audio for word in googwords):
        search(audio)
        exit()

    elif 'mail' in audio or 'email' in audio:
        sendmail()

    elif any(word in audio for word in calwords):
        calculate(audio)

    elif 'stop' in audio or 'exit' in audio:
        talk("good bye sir")
        exit()

    elif 'weather' in audio:
        weather()

    elif 'screenshot' in audio:
        screenshot()

    else:
        gentalk(audio)


i = 0
talk("welcome to the voice based search assistant")
while i <= 10:
    welcome()




