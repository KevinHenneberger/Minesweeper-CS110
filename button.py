class Button:

    # Button constructor 
    def __init__(self, y, text):
        self.x = 120
        self.y = y
        self.w = 150
        self.h = 50
        self.text = text
        self.textColor = (255, 255, 255)
        self.bgColor = (0, 0, 0)
        self.fgColor = (60, 60, 255)

    def mouseOver(self, mouseX, mouseY):
        """
        - return if the mouse is hovered over the button or not
        """
        return ((self.x <= mouseX <= self.x + self.w) and (self.y <= mouseY <= self.y + self.h))
