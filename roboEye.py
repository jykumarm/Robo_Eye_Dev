from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QFont

from EcgDetector import *
import pyscreenshot as ImageGrab

import sys
import tempfile
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

import pyttsx3


import time



import time
import traceback, sys

font_but = QtGui.QFont()
font_but.setFamily("Segoe UI Symbol")
font_but.setPointSize(15)
font_but.setWeight(100)


class PushBut1(QtWidgets.QPushButton):
    
    def __init__(self, parent=None):
        super(PushBut1, self).__init__(parent)
        self.setMouseTracking(True)
        self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
                           "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")
        

    def enterEvent(self, event):
        if self.isEnabled() is True:
            self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,230,255,255);"
                               "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,230,255,255);")
        if self.isEnabled() is False:
            self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
                               "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")

    def leaveEvent(self, event):
        self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
                           "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")



class QThread1(QtCore.QThread):
    sig1 = pyqtSignal(str)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
    def on_source(self, txt):
        #print(txt)'
        self.source_txt = txt 
    def run(self):
        print("caledddddddddddddddddddddddddddddddddddddd")
        if self.source_txt:
            engine = pyttsx3.init()
            engine.setProperty('rate',120)
            engine.setProperty('volume', 100)
            engine.say(self.source_txt + " pattern is detetcted!")
            engine.runAndWait()

            
class PyQtApp(QtWidgets.QWidget):
    is_Start = False
    status_message = "Results..mmmmmmmmmmmmmmmmmmmmmmmmmmm"
    ecgDetector = None
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("RoBo Eye-Cardio Analyzer")
        self.setWindowIcon(QtGui.QIcon("Path/to/Your/image/file.png"))
        self.setFixedWidth(1200)
        self.setFixedHeight(350)
##        self.setMinimumWidth(resolution.width() / 3)
##        self.setMinimumHeight(resolution.height() / 1.5)
        self.setStyleSheet("QWidget {background-color: rgba(0,41,59,255);} QScrollBar:horizontal {width: 1px; height: 1px;"
                           "background-color: rgba(0,41,59,255);} QScrollBar:vertical {width: 1px; height: 1px;"
                           "background-color: rgba(0,41,59,255);}")
        

        self.thread1 = QThread1()
        self.thread1.sig1.connect(self.thread1.on_source)
     
        models_dir = 'E:\\models\\'    
        self.ecgDetector = EcgDetector(models_dir)
        
        self.lbl2 = QtWidgets.QLabel(self)
        self.lbl2.setFixedWidth(630)
        self.lbl2.setFixedHeight(35)
        
##        self.lbl2.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(0,255,255,100); color: rgba(255,255, 255, 0);"
##                                 "border-style: solid; border-radius: 4px; border-width: 0.5px; border-color: rgba(0,140,255,255); ")

        font = QFont('Times', 12)
        self.lbl2.setFont(font)
        font.setWeight(95)
        #self.lbl2.setFontPointSize(12)
        self.lbl2.setText("Results...")
        self.lbl2.setFont(font)
                
        self.lbl2.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(0,255,255,0); color: rgba(255,255, 255, 0);"
                                 "border-style: solid; border-radius: 4px; border-width: 0.5px; border-color: rgba(0,255,255,0); ")
       

        self.lbl2.move(210,220)
         
        self.but1 = PushBut1(self)
        self.but1.setText("⯈")
        self.but1.setFixedWidth(72)
        self.but1.setFixedHeight(35)
        self.but1.setFont(font_but)

        self.but2 = PushBut1(self)
        self.but2.setText("⯀")
        self.but2.setFixedWidth(72)
        self.but2.setFixedHeight(35)
        self.but2.setFont(font_but)

        self.lb1 = QtWidgets.QLabel(self)
        self.lb1.setFixedWidth(800)
        self.lb1.setFixedHeight(160)
        self.lb1.move(40,40)
        self.lb1.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(0,255,255,100); color: rgba(0,190,255,255);"
                                 "border-style: solid; border-radius: 4px; border-width: 0.1px; border-color: rgba(0,140,255,255);")

         
##        self.textf.setStyleSheet("margin: 1px; padding: 7px;"
##                                 "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
        
        #self.grid1 = QtWidgets.QGridLayout()
##        self.grid1.addWidget(self.textf, 0, 0, 14, 13)
        self.but1.move(40,220)
        self.but2.move(120,220)
   #     self.grid1.addWidget(self.but2, 1, 28, 1, 1)
##        self.grid1.addWidget(self.but3, 2, 14, 1, 1)
        #self.grid1.addWidget(self.but4, 3, 14, 1, 1)
##        self.grid1.addWidget(self.but5, 4, 14, 1, 1)
##        self.grid1.addWidget(self.but6, 5, 14, 1, 1)
##        self.grid1.addWidget(self.but7, 6, 14, 1, 1)
        
      #  self.grid1.setContentsMargins(7, 7, 7, 7)
       # self.setLayout(self.grid1)
        self.but1.clicked.connect(self.on_but1)
        self.but2.clicked.connect(self.on_but2)
    
    def on_but1(self):
        #self.textf.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,217,100); color: rgba(0,190,255,255);"
                                 #"border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
       # print("clicked")
        self.is_Start = True
        
        test_img = 'E:\\brady.png'
        models_dir = 'E:\\models\\'

##        self.lb1 = QtWidgets.QLabel(self)
##        self.lb1.setFixedWidth(900)
##        self.lb1.setFixedHeight(160)
        pixmap = QPixmap('E:\\models\\brady-full.png')
        self.lb1.setPixmap(pixmap)
        self.lb1.setAlignment(QtCore.Qt.AlignCenter)
        #self.grid1.addWidget(self.lb1, 0, 0, 1, 1)
##        self.lb1.move(150,50)
        i = 0;
        currentEvent = None
        while(self.is_Start):
            #print("inside while")
            i = i+ 1;
           # print(i);
        
            im = ImageGrab.grab(bbox = (100, 140, 900,300));
            im.save(test_img);
            rslt = self.ecgDetector.compare(test_img)
            if (rslt != currentEvent):
                self.thread1.sig1.emit(rslt)
                self.thread1.start()
                self.eventLabelUpdate(rslt)
            currentEvent = rslt
           # print(self)
##            if rslt:
##                self.thread1 = QThread1()
##                self.thread1.sig1.connect(self.thread1.on_source)
##                self.thread1.sig1.emit(rslt)
##                self.thread1.start()
          
            pixmap = QPixmap('E:\\res.png')
            self.lb1.setPixmap(pixmap)
            QApplication.processEvents()
        
        ##self.initUI();
  
    
    def on_but2(self):
       self.is_Start = False

    def eventLabelUpdate(self,event_label):
        #print ("hello update")
        if event_label:
            self.lbl2.setText(event_label + " pattern detected!!!")
            self.lbl2.setStyleSheet("margin: 1px; background-color: rgba(255,0,0,1); color: rgba(255,255,255,1);"
                                     "border-style: solid; border-radius: 4px; border-width: 0.1px; border-color: rgba(0,140,255,255);")
        else:
             self.lbl2.setText("")
             self.lbl2.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(255,0,0,0); color: rgba(255,255, 255, 0);"
                                 "border-style: solid; border-radius: 4px; border-width: 0.5px; border-color: rgba(255,0,0,0); ")
             
        
 
    def initUI(self):
        print("clicked")
        
        test_img = 'E:\\brady.png'
        models_dir = 'E:\\models\\'

##        self.lb1 = QtWidgets.QLabel(self)
##        self.lb1.setFixedWidth(900)
##        self.lb1.setFixedHeight(160)
        pixmap = QPixmap('E:\\models\\brady-full.png')
        self.lb1.setPixmap(pixmap)
        self.lb1.setAlignment(QtCore.Qt.AlignCenter)
        #self.grid1.addWidget(self.lb1, 0, 0, 1, 1)
##        self.lb1.move(150,50)
        i = 0;
       
        while(self.is_Start):
            print("inside while")
            i = i+ 1;
            print(i);
        
            im = ImageGrab.grab(bbox = (100, 140, 900,300));
            im.save(test_img);
            rslt = compare(test_img, models_dir)
            print(self)
##            if rslt:
##                self.thread1 = QThread1()
##                self.thread1.sig1.connect(self.thread1.on_source)
##                self.thread1.sig1.emit(rslt)
##                self.thread1.start()
          
            pixmap = QPixmap('E:\\res.png')
            self.lb1.setPixmap(pixmap)
            QApplication.processEvents()
            
    def updateEventInfo(self):
        print("Do action here!") 

        print("Do action here!")
        
        


















if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
    myapp = PyQtApp()
    myapp.show()

   

##    myapp.threadpool = QThreadPool()
##    print("Multithreading with maximum %d threads" % myapp.threadpool.maxThreadCount())
##



    #myapp.setWindowOpacity(0.95)
    #myapp.show()
    #Smyapp.move(resolution.center() - myapp.rect().center())
    sys.exit(app.exec_())
else:
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
    
