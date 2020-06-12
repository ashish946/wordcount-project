from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')


def count(request):
    tarea=request.GET['tarea']
    tcount=tarea.split()
    d={}
    for word in tcount:
        d[word]=d.get(word,0)+1
    di=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'text':tarea,'wordlen':len(tcount),"words":di})

def about(request):
    return render(request,'about.html')
