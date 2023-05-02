import sys
import time
from Controller.Player_controller import PlayerController

# Run our program
def main():
    app = PlayerController()
    sys.exit(app.run())

    
if __name__ == '__main__':
    main()