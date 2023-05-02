import os
import simpleaudio
from pydub import AudioSegment
from pydub import playback


class Player:
    def __init__(self):
        self.songs = {}
        self._get_songs()
        self.play_obj = None

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

    def play_song(self, song, start_ms):
        self.play_obj = playback._play_with_simpleaudio(self.songs[song][start_ms:])

    def stop_song(self):
        if self.play_obj:
            self.play_obj.stop()
            self.play_obj = None