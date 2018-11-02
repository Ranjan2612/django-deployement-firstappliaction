from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'Html/index.html')

def Movie_view(request):
    return render(request,'Html/Movie.html')

def news_view(request):
    return render(request,'Html/news.html')

def sports_view(request):
    return render(request,'Html/sports.html')            
