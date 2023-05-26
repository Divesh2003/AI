class waterjug:
    def __init__(self, am, bm, a, b, g):
        self.a_max = am
        self.b_max = bm
        self.a = a
        self.b = b
        self.goal = g

    def printw (self):
        print(f"({self.a},{self.b})")

    def fillA(self):
        self.a = self.a_max
        self.printw()

    def emptyB(self):
        self.b = 0
        self.printw()
    def transferAtoB(self):
        while True:
            self.a = self.a-1
            self.b = self.b+1
            if self.a == 0 or self.b== self.b_max:
                break
        self.printw()

    def main(self):
        while True:
            if self.a == self.goal or self.b == self.goal:
                break
            if self.a == 0:
                self.fillA()
            elif self.a > 0 and self.b != self.b_max:
                self.transferAtoB()
            elif self.a > 0 and self.b == self.b_max:
                self.emptyB()

wj = waterjug(5 ,3 ,0 ,0 ,4)
wj.main()