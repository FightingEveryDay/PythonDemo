from django.shortcuts import render
from .models import BBS

# Create your views here.
def index(request):
    bbs_lists = BBS
    return render((request,'app01/index.html',{'bbs_lists':bbs_lists}))
