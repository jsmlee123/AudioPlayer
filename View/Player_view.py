from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PlayerView(QWidget):

    change_vol = pyqtSignal()
    song_select = pyqtSignal()
    stop = pyqtSignal()
    start = pyqtSignal()


    def __init__(self) -> None:
        '''
        Init non-gui members of class
        '''
        super(PlayerView, self).__init__()
        self.songs = set()
        self.curr_song_len = 500 #sec
        self.curr_song = "None"
        self._initUI()

    def _initUI(self):

        #Add background image
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('QWidget {background-image: url(View//background.jpg);}')

        self.setFixedSize(800,400)
        self.setWindowTitle("Audio Player")

        # song list view
        self.list_view = QListWidget(self)
        self.list_view.resize(175, 400)
        self.list_view.move(625, 0)
        self.list_view.itemClicked.connect(self.song_select)


        # slider for song position
        self.song_slider = QSlider(Qt.Horizontal, self)
        self.song_slider.resize(500, 20)
        self.song_slider.move(50, 300)
        self.song_slider.setRange(0, self.curr_song_len)
        self.song_slider.setValue(0)

        self.song_slider.valueChanged.connect(self.update_time)


        # slider for volume
        self.vol_slider = QSlider(Qt.Vertical, self)
        self.vol_slider.resize(20, 200)
        self.vol_slider.move(10, 20)
        self.vol_slider.setRange(-100, 100)
        self.vol_slider.setValue(0)
        self.vol_slider.valueChanged.connect(self.update_vol)
        self.vol_slider.sliderReleased.connect(self.change_vol)

        #volume label
        self.vol_label = QLabel("0", self)
        self.vol_label.resize(50, 20)
        self.vol_label.move(15, 225)

        #time label
        self.time_label = QLabel("00:00", self)
        self.time_label.resize(50, 20)
        self.time_label.move(300, 270)

        #song label
        self.song_label = QLabel("", self)
        self.song_label.resize(300, 20)
        self.song_label.move(240, 350)

        #play button
        self.play_button = QPushButton(">", self)
        self.play_button.resize(30, 30)
        self.play_button.move(290, 320)
        self.play_button.clicked.connect(self.start)

        #stop button
        self.stop_button = QPushButton("||", self)
        self.stop_button.resize(30, 30)
        self.stop_button.move(320, 320)
        self.stop_button.clicked.connect(self.stop)

    def set_song(self, song):
        self.curr_song = song
        self.song_label.setText(f'Playing : {song}')

    def add_songs(self, songs):
        for s in songs:
            self.songs.add(s)

    def get_selected(self):
        return [s.text() for s in self.list_view.selectedItems()]

    def get_volume(self):
        return self.vol_slider.value()

    def update_vol(self, val):
        self.vol_label.setText(f'{val}')

    def update_time(self, val):
        self.time_label.setText(f'{val // 60}'.zfill(2) + ":" + f'{val % 60}'.zfill(2))
    
    def display_songs(self):
        for song in self.songs:
            QListWidgetItem(song, self.list_view)
        