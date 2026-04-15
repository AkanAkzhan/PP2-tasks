
class Ball:

    def __init__(self,x,y,radius,step,width,height):
        self.x = x
        self.y = y
        self.radius = radius
        self.step = step
        self.width = width
        self.height = height

    def move_up(self):

        if self.y - self.step >= self.radius:
            self.y -= self.step

    def move_down(self):

        if self.y + self.step <= self.height - self.radius:
            self.y += self.step

    def move_left(self):

        if self.x - self.step >= self.radius:
            self.x -= self.step
    
    def move_right(self):
        if self.x + self.step <= self.width - self.radius:
            self.x += self.step
    
