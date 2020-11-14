from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render (request,"App/index.html")


def submit(request):

    q=request.GET['query']
    try:
        a= eval(q)
        mdict = {
            'ans': a,
            'q': q,
            'error': False
        }

        return render(request,'app/index.html',context=mdict)

    except:

           mdict = {

               'error': True
           }

           return render(request, 'app/index.html', context=mdict)