from django.shortcuts import render

# Create your views here.
def hello_world(request):
  return render(request,'website/home.html')

def about(request):
  return render(request,'on about page')