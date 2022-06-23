from django.shortcuts import render

import subprocess


def home(request):
    context = {}

    proc = subprocess.Popen("dir", stdout=subprocess.PIPE, shell=True)

    dirlist = str(proc.stdout.read())
    context['dirlist'] = dirlist

    return render(request, 'home.html', context)



