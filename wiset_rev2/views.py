from django.http import HttpResponse
from django.shortcuts import render

from .forms import MoneyForm


def index(request):
    if request.method == 'POST':
        form = MoneyForm(request.POST)
        if form.is_valid():
            return HttpResponse("mm nice")
    else:
        form = MoneyForm()
    return render(request, 'index.html', {'form': form})
