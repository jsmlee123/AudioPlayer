import sys
import time
from Model.Player import Player

# Run our program
def main():
    player = Player()
    player.set_song("Tell Me.mp3", 0)
    player.change_vol_idle(-40)
    player.play_song()
    time.sleep(10)
    player.change_vol_realtime(20)
    time.sleep(10)
    player.change_vol_realtime(10)
    time.sleep(1000)
    
if __name__ == '__main__':
    main()