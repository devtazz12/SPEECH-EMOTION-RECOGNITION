
from django.shortcuts import render, HttpResponse
from .models import Audio
from .predictions import LivePredictions
from django.views.decorators.csrf import csrf_exempt
from playsound import playsound
import pyaudio
import wave
import datetime
from .predictions import working_dir_path
import os
from django.contrib import messages
# Sampling frequency
freq = 44100
# Recording duration
duration = 5
 








def index(request):
    return render(request, 'index.html')


def audioSubmit(request):
    try:
        if request.method == 'POST':
            audiofile = request.FILES.get('audiofile')
            live_prediction = LivePredictions(file=audiofile)
            emotion=live_prediction.make_predictions()
            Audio.objects.all().delete()
            Audio.objects.create(title=audiofile, audio_file=audiofile).save()
            messages.success(request, "File has been succesfully uploaded click below to check result!")
        context ={
            'emotion':emotion,
            'audiofile':Audio.objects.get(title=audiofile)
        }
    except Exception as e:
        return HttpResponse("error: {}".format(e))

    return render(request, 'index.html', context)


def recording(request):  
    return render(request, 'recording.html')


@csrf_exempt
def recordingUpload(request):
    try:
        if request.method == 'POST':
            audio = pyaudio.PyAudio()
            stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
            start_time = datetime.datetime.now()
            duration=4
            frames = []
            try: 
                while (datetime.datetime.now() - start_time).total_seconds() < duration:
                    data = stream.read(1024)
                    frames.append(data)
            except KeyboardInterrupt:
                pass
            stream.stop_stream()
            stream.close()
            audio.terminate()

            soundfile = wave.open("recording.wav", 'wb')
            soundfile.setnchannels(1)
            soundfile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            soundfile.setframerate(44100)
            soundfile.writeframes(b''.join(frames))
            soundfile.close
    except Exception as e:
        return HttpResponse("Error: {}".format(e))
    path = os.path.join(working_dir_path, "recording.wav")
    context = {
        'path':path
    }
    return render(request, 'recording.html', context)



def recordedAudioSubmit(request):
    try:
        if request.method == 'POST':
            audiofile = request.FILES.get('audiofile')
            live_prediction = LivePredictions(file=audiofile)
            emotion=live_prediction.make_predictions()
            Audio.objects.all().delete()
            Audio.objects.create(title=audiofile, audio_file=audiofile).save()
            messages.success(request, "File has been succesfully uploaded click below to check result!")
        context ={
            'emotion':emotion,
            'audiofile':Audio.objects.get(title=audiofile)
        }
    except Exception as e:
        return HttpResponse("error: {}".format(e))

    return render(request, 'recording.html', context)



