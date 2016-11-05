from django.shortcuts import render
from django.views.generic import  ListView  ,DetailView #list des objects
from .models import  Bd
def index(request):
    return render(request,'app/index.html')
class PostList(ListView):
    model = Bd

class PostDetail(DetailView):
    model = Bd
# Create your views here.
