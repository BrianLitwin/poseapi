from django.shortcuts import render

from .model import model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2

@csrf_exempt 
def img_keypoints(request):
    if request.method == 'POST':
        file = request.FILES.get('image')
        bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        image = cv2.imdecode(bytes, cv2.IMREAD_COLOR)
        keypoints = model(image)['points'].tolist()

        return JsonResponse({"keypoints": keypoints, 
                             "height": image.shape[0], 
                             "width": image.shape[1]})
    else:
        return JsonResponse({'error': 'Apparently, only POST requests allowed'})
