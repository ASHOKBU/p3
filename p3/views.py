from django.shortcuts import render

def third(request):
    return render(request,'directory/third.html',context={'data':"Ashok",'name':"Shankar"})

def fourth(request):
    fruits=["apple","banana","mango","grapes"]
    return render(request,'directory/fourth.html',context={'fruits':fruits})

def fifth(request):
    return render(request,'directory/fifth.html',context={'a':10,'b':20})