import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMovie


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barışma Minigame")
        #self.showFullScreen()
        self.setGeometry(0,0,1900,800)
        self.setMaximumSize(1920,1080)
        self.c_widget = QWidget(self)
        self.setCentralWidget(self.c_widget)

        self.pix_label = QLabel(self)
        movie = QMovie("animal.gif")
        movie.setScaledSize(QSize(400,400))
        self.pix_label.setMovie(movie)

        movie.start()
        self.main_label = QLabel("Seni Üzdüğüm için Üzgünüm.<br>Barışalım mı?")

        self.initUI()
    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.sub_layout = QHBoxLayout()

        #Üstteki Yazılar
        self.main_label.setAlignment(Qt.AlignCenter)
        self.main_label.setStyleSheet("font-size: 60px;"
                                      "font-family: Arial;"
                                      "font-weight: bold;"
                                      "margin: 100px")

        self.pix_label.setAlignment(Qt.AlignCenter)

        
        #Butonlar
        self.fixedwidth = 300
        self.fixedheight = 100
        self.acc_button = QPushButton(self)
        self.acc_button.setText("Evet")
        self.acc_button.setFixedSize(self.fixedwidth, self.fixedheight)
        self.acc_button.setStyleSheet("background-color: #2acf1b;" \
                                      "border: 1px solid;" \
                                      "border-radius: 10px;"
                                      "font-size: 30px;"
                                      "font-weight: bold;"
                                      "border-color: gray;")
        
        self.acc_button.clicked.connect(self.acc_button_toggled)
        
        self.no_button = QPushButton(self)
        self.no_button.setText("Hayır")
        self.no_button.setFixedSize(300,100)
        self.no_button.setStyleSheet("background-color: #cf1b1b;" \
                                      "border: 1px solid;" \
                                      "border-radius: 10px;"
                                      "font-size: 30px;"
                                      "font-weight: bold;"
                                      "border-color: gray;")
        self.no_button.clicked.connect(self.no_button_toggled)
        

        self.sub_layout.setSpacing(40)
        self.sub_layout.setAlignment(Qt.AlignCenter)
        self.sub_layout.addWidget(self.acc_button)
        self.sub_layout.addWidget(self.no_button)
        #Layout Düzenleme
        self.c_widget.setStyleSheet("background-color: white;")
        self.main_layout.addWidget(self.main_label)
        self.main_layout.addLayout(self.sub_layout)
        self.main_layout.addWidget(self.pix_label)
        self.mainspace = 40
        self.main_layout.setSpacing(self.mainspace)
        self.main_layout.setAlignment(Qt.AlignCenter)

        self.c_widget.setLayout(self.main_layout)


    def no_button_toggled(self):
        self.fixedheight += 75
        self.fixedwidth += 200
        self.acc_button.setFixedSize(self.fixedwidth, self.fixedheight)

        if  self.mainspace> 0:
            self.mainspace-=10
            self.main_layout.setSpacing(self.mainspace)
        
        else:
            pass
    def acc_button_toggled(self):
        self.main_label.setParent(None)
        self.main_label.deleteLater()
        self.acc_button.setParent(None)
        self.acc_button.deleteLater()
        self.pix_label.setParent(None)
        self.pix_label.deleteLater()
        self.no_button.setParent(None)
        self.no_button.deleteLater()
        self.alternativeUI()


    def alternativeUI(self):
        new_label = QLabel("Evet Diyeceğini biliyordum!<br> Teşekkür Ederim")
        new_label.setTextFormat(Qt.RichText)   # <-- burada eklendi
        new_label.setStyleSheet("font-size: 60px;"
                                "font-weight: bold")
        new_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(new_label)

        self.npix_label = QLabel(self)
        movie = QMovie("ustustekedi.gif")
        movie.setScaledSize(QSize(600, 600))  # Eğer istersen boyutlandırabilirsin
        self.npix_label.setMovie(movie)
        movie.start()
        self.npix_label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.main_layout.addWidget(self.npix_label)





app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())











