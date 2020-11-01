from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse

# Create your views here.

def payment(request):
    response = requests.post('https://testapi.yenepay.com/api/urlgenerate/getcheckouturl/',
    headers={'Content-Type': 'application/json'},
    json={"process":"Cart",
    "successUrl":"http://localhost:8000/api/v2/pay-success/",
    "merchantId":"0749",
    "merchantOrderId":"kajhk-kjh",
    "expiresAfter":24,
    "items":[
        {
            "itemId":"sku-01",

            "itemName":"Home cleaning",

            "unitPrice":230,

            "quantity":2

        },],

    "totalItemsDeliveryFee":10,

    "totalItemsTax1":2.3
    }
    )
    print(response.request.body)
    json_response = response.json()
    result = json_response['result']
    return redirect(result)

def paymentAcceptedSuccessfully(request):
    return HttpResponse('payment accepted succ.')