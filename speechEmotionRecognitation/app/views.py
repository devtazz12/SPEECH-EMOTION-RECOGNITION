
from django.shortcuts import render, redirect, HttpResponse

from .models import Audio
from .predictions import LivePredictions







def index(request):
    return render(request, 'index.html')

def audioSubmit(request):
    try:
        if request.method == 'POST'and request.FILES['audiofile']:
            audiofile = request.FILES.get('audiofile')
            live_prediction = LivePredictions(file=audiofile)
            emotion=live_prediction.make_predictions()
            Audio.objects.all().delete()
            Audio.objects.create(title=audiofile, audio_file=audiofile).save()
        context ={
            'emotion':emotion,
            'audiofile':Audio.objects.get(title=audiofile)
        }
    except Exception as e:
        return HttpResponse("error: {}".format(e))

    return render(request, 'index.html', context)









