from django.shortcuts import render
from testap.models import*
# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydinfo(request):
    jobs_list=hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hyd.html',context=my_dict)

def puneinfo(request):
    jobs1_list=punejobs.objects.all()
    my_dict={'jobs1_list':jobs1_list}
    return render(request,'testapp/pune.html',context=my_dict)

def baninfo(request):
    jobs2_list=bangjobs.objects.all()
    my_dict={'jobs2_list':jobs2_list}
    return render(request,'testapp/bang.html',context=my_dict)

def ndlinfo(request):
    jobs3_list=ndljobs.objects.all()
    my_dict={'jobs3_list':jobs3_list}
    return render(request,'testapp/nandyal.html',context=my_dict)
