from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .forms import dform, mform, eform
from .models import director, manager, engineer


def c_view(request):
    man_name = request.GET["manager"]
    man_set = manager.objects.filter(m_name=man_name)
    print(len(man_set))
    if len(man_set) > 0:
        e_set = man_set[0].engineer_set.all()
        print(len(e_set))
        return render_to_response('m2.html', {'engineer': e_set})
    else:
        return HttpResponse("no manager found")


def d_view(request):
    if request.method == 'POST':
        form = dform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = dform()
    return render_to_response('m1.html', {'form': form})


def m_view(request):
    if request.method == 'POST':
        form = mform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = mform()
    return render_to_response('m1.html', {'form': form})


def e_view(request):
    if request.method == 'POST':
        form = eform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = eform()
    return render_to_response('m1.html', {'form': form})
