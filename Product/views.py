from django.shortcuts import render
# Create your views here.
def action(request):
    #context = {}
    return render(request,"Product/index.html")
def blog(request):
    return render(request,"Product/blog.html")
