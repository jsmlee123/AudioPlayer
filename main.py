import sys
from Model.Player import Player

# Run our program
def main():
    player = Player()
    print(player.len_song("Tell Me.mp3"))
    player.play_song("Aruarian Dance.mp3", 0)
    sys.exit()
    
if __name__ == '__main__':
    main()