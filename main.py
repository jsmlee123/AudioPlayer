import sys
import time
from Controller.Player_controller import PlayerController

# Run our program
def main():
    '''
    player = Player()
    player.set_song("Tell Me.mp3", 0)
    player.change_vol_idle(-40)
    player.play_song()
    time.sleep(100)
    '''
    app = PlayerController()
    sys.exit(app.run())

    
if __name__ == '__main__':
    main()