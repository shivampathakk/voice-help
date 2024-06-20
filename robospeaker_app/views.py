import os
from django.shortcuts import render
from django.http import HttpResponse

def text_to_speech(text):
    # Using PowerShell to access built-in text-to-speech on Windows
    command = f'powershell -command "Add-Type -AssemblyName System.Speech; ' \
              f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
              f'$speak.Speak(\'{text}\')"'
    os.system(command)

def index(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            text_to_speech(text)
        return render(request, 'robospeaker_app/index.html', {'text': text})
    return render(request, 'robospeaker_app/index.html')
