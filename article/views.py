from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    word = text.split()
    word_directionaly = {}

    for word in word:
        if word in word_directionaly:
            word_directionaly[word]+=1
        else:
            word_directionaly[word]=1

    return render(request, 'result.html',{'full': text, 'total': len(word), 'dictionary': word_directionaly.items()})
