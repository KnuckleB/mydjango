import requests
from django.http import HttpResponse
from django.shortcuts import render
import json
from requests.auth import HTTPBasicAuth

from pills.credentials import MpesaAccessToken, LipanaMpesaPpassword


# Create your views here.


def home(request):
    return render(request, 'adminHome.html')


def appointment(request):
    return render(request, 'appointmentDetails.html')


def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def login(request):
    return render(request, 'login.html')


def member(request):
    return render(request, 'member.html')


def products(request):
    return render(request, 'products.html')


def register(request):
    return render(request, 'register.html')


def upload(request):
    return render(request, 'upload.html')


def users(request):
    return render(request, 'users.html')


def add(request):
    return render(request, 'add.html')


def edit(request):
    return render(request, 'edit.html')


def pay(request):
    return render(request, 'pay.html')


def show(request):
    return render(request, 'show.html')


def image(request):
    return render(request, 'show_image.html')


def picture(request):
    return render(request, 'upload_image.html')


def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token": validated_mpesa_access_token})


def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")
