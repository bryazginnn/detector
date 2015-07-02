# -*- coding: utf-8 -*-
import utils
  
def prepare(imgPath, detector, w, h):
    '''
    Чтение изображения, resize, возвращение подготовленного для сравнения объекта(-ов)
    
    :param imgPath: путь до изображения
    :param detector: путь до изображения
    :param w: ширина изображения после resize
    :param h: высота изображения после resize
    
    :returns kp: особые точки изображения
    :returns desc: описания особых точек изображения
    '''
    img = utils.read(imgPath)
    img = utils.resize(img, w, h)
    if not detector:
        raise Exception("Detector can't be None")
    kp, desc = detector.detectAndCompute(img, None)
    return kp, desc