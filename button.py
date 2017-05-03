class Button:    #This class describes the buttons that are to be used in the game of Minesweeper. A button has a geometrical area that, when clicked, instructs the program to take some action. Depending on the button, this action is either to send the player to a specific screen, or to change the difficulty of the game. Each button also has text on it, explaining what the action represented by the button is.

    # Button constructor 
    def __init__(self, y, text):    #This method asks for the vertical location of the button and the text displayed on the button.
        self.x = 120    #The x-coordinates of the button's location.
        self.y = y      #The y-coordinate of the button's location. x is fixed, and y is variable, so the button locations range along a vertical line.
        self.w = 150    #The width of the button.
        self.h = 50     #The height of the button.
        self.text = text            #The text displayed on the button.
        self.textColor = (255, 255, 255)    #This sets the color of the text displayed on the button. The color is white.
        self.bgColor = (0, 0, 0)      #This sets the background color of the button to black.
        self.fgColor = (60, 60, 200)      #This sets the foreground color of the button to blue.

    def mouseOver(self, mouseX, mouseY):    #mouseX and mouseY are, respectively, the x- and y-coordinates of the mouse pointer.
        """
        - return if the mouse is hovered over the button or not
        """
        return ((self.x <= mouseX <= self.x + self.w) and (self.y <= mouseY <= self.y + self.h))    #Determine whether the mouse pointer is within the coordinates that geometrically bound the button (i.e. within its perimeter).

