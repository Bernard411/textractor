from django.shortcuts import render
from .form import ImageUploadForm
from .models import ImageData
from PIL import Image
import pytesseract


def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            img_obj = Image.open(img)  
            img_obj = img_obj.convert('L')
            text = pytesseract.image_to_string(img_obj)
            imagedata = ImageData(image=img) 
            imagedata.save() 
            return render(request, 'index.html', {'text': text, 'image': imagedata})
    else:
        form = ImageUploadForm()
 
    imagedata= ImageData.objects.all()
    context = {'form': form, 'imagedata': imagedata}
    return render(request, 'index.html', context)
