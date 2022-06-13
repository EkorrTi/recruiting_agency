import imp
from django.shortcuts import render
from accounts.models import Account
# Create your views here.
def manager_screen(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'base.html', context)