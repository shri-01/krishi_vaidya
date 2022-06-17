from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.backend import set_session
import numpy as np


def prepare_image(path):
    img = load_img(path, target_size=(224,224))
    img = img_to_array(img)
    img = img/255
    img = np.expand_dims(img, axis=0)
    return img

# return render(request, 'home/home.html')

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def analysis(request):
    if(request.method == 'POST'):
        file = request.FILES['imageFile']
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)

        img = prepare_image(file_url)

        #Disease Classes
        s = {0:'Early Blight Disease',1:'Healthy Plant',2:'Late Blight Disease',3:'Septorial Diseased Plant',
                4:'Yellow Leaf Curl Virus'}

        with settings.GRAPH1.as_default():
            set_session(settings.SESS)
            predictions = settings.IMAGE_MODEL.predict(img)
            predict = np.argmax(predictions)
            predictions = s[predict]
            return render(request, "home/analysis.html", {"predictions": predictions})

    else:
        return render(request, "home/analysis.html")
    return render(request, "home/analysis.html")

def early_blight(request):
    return render(request, 'home/early _bligth.html')

def late_bligth(request):
    return render(request, 'home/late_bligth.html')

def Septorial_Disease(request):
    return render(request, 'home/Septorial_Disease.html')

def yellow_curl(request):
    return render(request, 'home/yellow_curl.html')
