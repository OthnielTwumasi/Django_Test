from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "name":"Othniel",
        "age":5,
        "food": "Mr Wu's"
    }
    return render(request,"myapp/index.html",context)