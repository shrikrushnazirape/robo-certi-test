from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Student
from PIL import Image, ImageFont, ImageDraw
import os

def index(request):
    if request.method == "POST":
        data = request.POST
        email = data['email']
        roll = data['roll_no']
        try:
            getuser = Student.objects.get(email_id = email)
            if(getuser and getuser.roll_no == roll):
                certificate= Image.open("media/bootcamp_temp_certi.png")
                name_font = ImageFont.truetype("media/fonts/LibreBaskerville-Italic.ttf",60)
                image_editable = ImageDraw.Draw(certificate)
                image_editable.text((500,550), getuser.name, (24, 16, 74),font=name_font)
                certificate.save('media/'+str(getuser.roll_no)+'.png')
                # # return ('certificates/'+str(name)+'.png')
                certiurl = 'media/'+str(getuser.roll_no)+'.png'
                return render(request, 'userapp/success.html', {'user':getuser, 'certi':certiurl})
            return HttpResponse("invalid user data1")
        except Exception as e:
            print(e)
            return HttpResponse("invalid user data2")
     
    return render(request, 'userapp/index.html')
