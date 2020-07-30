from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

def hospital(request):
    hospital = Hospital.objects.all()
    return render(request, 'hospital.html', {'list':hospital})
    # html=''
    # for h in hospital:
    #     html += '%s %s %s %s %s %s %s <br><br>' %(h.id, h.sido, h.name, h.medical, h.room, h.tel, h.address) 
    # return HttpResponse(html)

def index1(request):
    return HttpResponse('index1')

def main(request):
    return HttpResponse('main!')
# Create your views here.
