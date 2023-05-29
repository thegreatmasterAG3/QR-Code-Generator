from django.shortcuts import render

# Create your views here.



# qrcodeapp/views.py

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time


# def qr_gen(request):
#     if request.method == 'POST':
#         data = request.POST['data']
#         img = make(data)
#         img_name = 'qr' + str(time.time()) + '.png'
#         img.save(str(settings.MEDIA_ROOT / img_name))  # Convert WindowsPath to string
#         return render(request, 'index.html', {'img_name': img_name})
#     return render(request, 'index.html')



from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from .models import QRCode

def qr_gen(request):
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img_path = str(settings.MEDIA_ROOT / img_name)
        img.save(img_path)  # Convert WindowsPath to string

        # Save the QR code image in the database
        qr_code = QRCode.objects.create(image=img_name)
        



        return render(request, 'index.html', {'img_name': img_name})
    return render(request, 'index.html')

