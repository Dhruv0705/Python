from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HomePageView(request,*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def AboutPageView(request,*args, **kwargs):
    #return HttpResponse("<h1>About Page</h1>")
    MyContext = {
        "MyText"    : "This is about us",
        "MyNumber"  : 123,
        "MyList"    : [123, 4567, 312, "ABC"],
        "Title"     : "This is about us",
        "IsTrue"    : True,
        "MyHtml"    : "<h1>Hello World</h1"
    }

    return render(request, "about.html", MyContext)

def ContactPageView(request,*args, **kwargs):
    #return HttpResponse("<h1>contact Page</h1>")
    return render(request, "contact.html", {})

