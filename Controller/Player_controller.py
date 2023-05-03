import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Model.Player import Player
from View.Player_view import PlayerView

class PlayerController:
    '''
    Controller to interact between player model and view
    '''
    def __init__(self) -> None:
        '''
        Init view and model
        '''
        self._app = QApplication(sys.argv)
        self._model = Player()
        self._view = PlayerView()
        self._connect_signals()
        self._add_songs()


    def _connect_signals(self):
        self._view.song_select.connect(self.select_song)
        self._view.start.connect(self.start_song)
        self._view.stop.connect(self.stop_song)
        self._view.change_vol.connect(self.change_vol)
        self._view.update.connect(self.update_time)
        self._view.jump.connect(self.jump_time)
    
    def jump_time(self):
        if not self._model.has_song():
            return
        self._model.set_song_pos(self._view.get_time() * 1000)
        if self._model.is_playing():
            self._model.stop_song()
            self._model.play_song()
    
    def update_time(self):
        self._view.set_time_slider(self._model.get_song_time_ms() // 1000)
        self._view.start_timer()
    
    def change_vol(self):
        self._model.change_vol(self._view.get_volume())
    
    def start_song(self):
        if not self._model.has_song():
            return
        self._model.play_song()
        self._view.start_timer()
    
    def stop_song(self):
        if not self._model.has_song():
            return
        self._model.stop_song()
        self._view.stop_timer()

    def select_song(self): 
        song = self._view.get_selected()[0]
        self._model.set_song(song, 0)
        self._model.change_vol_idle(self._view.get_volume())
        self._view.set_song(song)
        self._view.set_song_slider_max(round(self._model.len_song(song)))
        self._view.stop_timer()
        self._view.set_time_slider(0)

    def _add_songs(self):
        self._view.add_songs(self._model.get_songs())
        self._view.display_songs()

    def run(self):
        '''
        Run app
        '''
        self._view.show()
        return self._app.exec_()