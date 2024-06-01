from django.shortcuts import render

# Create your views here.
import pyttsx3

def converter(request):
    text=pyttsx3.init()
    name1=request.POST.get('name')
    text.setProperty('voice', 'english+f3')
    text.say(name1)
    return render(request,'next.html',text.runAndWait())

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print("ID:", voice.id)
    print("Name:", voice.name)
    print("Languages:", voice.languages)
    print("Gender:", voice.gender)
    print("Age:", voice.age)
    print("\n")
