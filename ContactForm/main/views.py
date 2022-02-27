from django.shortcuts import render
from .models import *
import requests
def Contacts(request):
    contact = Contact.objects.all()
    context = {
        'contact': contact,
    }
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            lastname=request.POST.get("lastname"),
            email=request.POST.get("email"),
            number=request.POST.get("number"),
            news=request.POST.get("news"),
        )
        token = "Bot fatherda ochgan botingizni tokenini shu so'zlar o'rniga qo'yasiz"
        text = "Sizga xabar yuborishdi: \n\n Ism: " + request.POST.get('name') + '\n Familiya: ' + request.POST.get("lastname") + '\n Email: ' + str(request.POST.get("email")) + '\n Telefon raqam: ' + str(request.POST.get("number")) + '\n Xabari: ' + request.POST.get('news')
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + str(Bu yerga esa ozingizni telegram profilingizni idisini yozasiz huddi videoda orgatilgandek) + '&text=' + text)
    return render(request, 'contact.html', context)