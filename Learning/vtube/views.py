from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'vtube/index.html')

def play(request):
     return render(request, 'vtube/play-video.html')
