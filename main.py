import turtle


class Turtle2(turtle.Turtle):

    def set_step(self, step):
        self.step = step

    def up(self, n=1):
        self.left(90)
        self.forward(self.step * n)
        self.right(90)

    def upr(self, n=1):
        self.left(45)
        self.forward(self.step * n * 1.41421356237)
        self.right(45)

    def upl(self, n=1):
        self.left(135)
        self.forward(self.step * n * 1.41421356237)
        self.right(135)

    def dwn(self, n=1):
        self.right(90)
        self.forward(self.step * n)
        self.left(90)

    def dwnr(self, n=1):
        self.right(45)
        self.forward(self.step * n * 1.41421356237)
        self.left(45)

    def dwnl(self, n=1):
        self.right(135)
        self.forward(self.step * n * 1.41421356237)
        self.left(135)

    def rgh(self, n=1):
        self.forward(self.step * n)

    def lft(self, n=1):
        self.right(180)
        self.forward(self.step * n)
        self.right(180)


image = Turtle2()
image.set_step(40)

ss = input()
i = 0
while i < len(ss):
    print(i)
    if ss[i] in ['↗', '↘', '↙', '←', '↖', '↓', '↑', '→']:
        if (i + 1) < len(ss):
            if ss[i + 1].isdigit():
                nn = int(ss[i + 1])
            else:
                nn = 1
        else:
            nn = 1
    if ss[i] in ['↗']:
        image.upr(nn)
    if ss[i] in ['↘']:
        image.dwnr(nn)
    if ss[i] in ['↙']:
        image.dwnl(nn)
    if ss[i] in ['↖']:
        image.upl(nn)

    if ss[i] in ['↑']:
        image.up(nn)
    if ss[i] in ['↓']:
        image.dwn(nn)
    if ss[i] in ['←']:
        image.lft(nn)
    if ss[i] in ['→']:
        image.rgh(nn)

    i += 1

turtle.exitonclick()
