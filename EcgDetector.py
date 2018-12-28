import cv2
import os
import glob
import pyscreenshot as ImageGrab
import numpy as np
from matplotlib import pyplot as plt

#screen shot taken


class Model(object):

    def __init__(self, model_name,template):
        self.name = model_name.replace(".png", "")
        self.template = template

class EcgDetector(object):
    
    models = []
    
    def __init__(self,models_dir):
        for img in glob.glob(models_dir + "*." + "png"):
             self.models.append(Model(img,cv2.imread(img,0)))

    def compare(self,test_img):
        threshold = 0.8
        matched_model = None
        img_rgb = cv2.imread(test_img)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        # iterate over available models
        for model in self.models:
##        for img in glob.glob(models_dir + "*." + "png"):
##            #print(img)
##            template = cv2.imread(img,0)
            w, h = model.template.shape[::-1]
            res = cv2.matchTemplate(img_gray,model.template,cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)

            if(np.any(loc)):
                matched_model = os.path.basename(model.name)
                
                # mark identified area
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                break;
        cv2.imwrite('E:\\res.png',img_rgb)
        return matched_model
##i = 0;
##while(True):
##    i = i+ 1;
##    print(i);
##    im = ImageGrab.grab();
##    im.save("test.png");
##    #im.show() got it
##    print(compare(test_img))





##cv_image = []
##for img in glob.glob("E:/models/*.png"):
##    template = cv2.imread(img,0) 
##    w, h = template.shape[::-1]
##    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
##    loc = np.where( res >= threshold)
##    print(img)
##    if(np.any(loc)):
##        break
    
#template = cv2.imread('E:/normal-ecg.png',0)






##loc = np.where( res >= threshold)
##print(loc)
##print(np.any(loc))



#def isValid
