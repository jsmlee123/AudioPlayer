import os
import time
import simpleaudio
from pydub import AudioSegment
from pydub import playback 


class Player:
    def __init__(self):
        self.songs = {}
        self._get_songs()
        self.play_obj = None
        self.curr_song = None
        self.curr_song_name = ""
        self.song_pos = 0
        self.song_elapse = 0

    def _get_songs(self):
        AudioSegment.converter = os.getcwd()+ "\\ffmpeg.exe"                    
        AudioSegment.ffprobe   = os.getcwd()+ "\\ffprobe.exe"
        path  = "../AudioPlayer/songs/"
        dir_list = os.listdir(path)
        for song in dir_list:
            if song[-3:] != "mp3": 
                continue
            self.songs[song] = AudioSegment.from_mp3(path + song)
    
    
    def len_song(self, song):
        if song in self.songs:
            return self.songs[song].duration_seconds
        return -1

    def set_song(self, song, start_ms):
        if self.play_obj and self.play_obj.is_playing():
            self.play_obj.stop()
        self.curr_song = self.songs[song]
        self.curr_song_name = song
        self.song_pos = start_ms
    
    def get_songs(self):
        return self.songs.keys()

    def play_song(self):
        if self.play_obj and self.play_obj.is_playing():
            return
        self.play_obj = playback._play_with_simpleaudio(self.curr_song[self.song_pos:])
        self.song_elapse = time.time()

    def change_vol_idle(self, val):
        self.curr_song = self.songs[self.curr_song_name]
        self.curr_song += val

    def change_vol(self, val):
        if self.play_obj:
            self.change_vol_realtime(val)
        

    def change_vol_realtime(self, val):
        self.curr_song = self.songs[self.curr_song_name]
        self.curr_song += val
        self.stop_song()
        self.song_pos = self.song_pos + 1000 * (time.time() - self.song_elapse) + 1
        self.play_song()
        self.song_elapse = time.time()

    def stop_song(self):
        self.play_obj.stop()
        self.song_pos = self.song_pos + 1000 * (time.time() - self.song_elapse) + 1
        self.song_elapse = time.time()
        
           