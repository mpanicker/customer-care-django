from django.shortcuts import render
from django.http import HttpResponse

from .models import AccountInfo

def index(request):
    all_accounts = AccountInfo.objects.all()
    return HttpResponse(all_accounts)

# Create your views here.
def getAccount(request, account_id):
    indiv_account = AccountInfo.objects.get(account_id=account_id)
    return HttpResponse("You're looking at account %s." % indiv_account.cust_name)

def getAccountDevices(request, account_id):
    indiv_account = AccountInfo.objects.get(account_id=account_id)
    devices = indiv_account.devices
    return HttpResponse("Account's devices %s." % devices)