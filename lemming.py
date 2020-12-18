import pyxel


class GameLemmings:
    def __init__(self, grounds, x, y):
        self.width = 15
        self.height = 15
        self.direct = 1
        self.x = x * 16
        self.y = y * 16
        self.pos_counter = 0
        self.grounds = grounds
        self.saved = 0
        self.umbrella_state = False

    def ground(self, p0, p1):
        if -1 < p0 < 256 and -1 < p1 < 256:
            if self.grounds[int(p0) // 16][int(p1) // 16] != 1:
                return True
            else:
                return False
        else:
            return True

    def exit(self, x, y):
        self.saved += 1
        if -1 < x < 256 and -1 < y < 256:
            if self.grounds[int(x) // 16][int(y) // 16] == 3:
                return True
            else:
                return False
        else:
            return True

    def umbrella(self, x, y):
        if -1 < x < 256 and -1 < y < 256:
            if self.grounds[int(x) // 16][int(y) // 16] == 4:
                return True
            else:
                return False
        else:
            return True

    def ladder_r(self, x, y):
        if -1 < x < 256 and -1 < y < 256:
            if self.grounds[int(x) // 16][int(y) // 16] == 5:
                return True
            else:
                return False
        else:
            return True

    def ladder_l(self, x, y):
        if -1 < x < 256 and -1 < y < 256:
            if self.grounds[int(x) // 16][int(y) // 16] == 6:
                return True
            else:
                return False
        else:
            return True

    # update position
    def update(self, l_lemmingsU, i):
        if -1 < self.x < 256 and -1 < self.y < 256:
            # MOVEMENT CHARACTERISTICS FOR THE RIGHT
            if self.direct == 1:
                # To make the lemming fall with the umbrella
                if self.umbrella(self.x, self.y) and self.ground(self.x, self.y + 16):
                    self.y += 16
                    self.umbrella_state = True
                elif self.ground(self.x, self.y + 16) and self.umbrella_state:
                    self.y += 16
                    if not self.ground(self.x, self.y + 16):
                        self.umbrella_state = False
                elif self.ground(self.x, self.y + 16) and not self.umbrella_state:
                    self.y += 16
                    self.pos_counter += 1
                    if self.pos_counter > 1:
                        del (l_lemmingsU[i])
                # To move it to the right when the next cell isn't a block
                if not self.ground(self.x, self.y + 16) and self.ground(self.x + 16, self.y):
                    self.x += 16
                # To change direction if the next cell is a block
                if not self.ground(self.x + 16, self.y):
                    self.direct = -1
                #To save the lemmings
                if self.exit(self.x - 16, self.y):
                    del (l_lemmingsU[i])
                #To go up to the right with the ladder
                if self.ladder_r(self.x, self.y):
                    for i in range(16):
                        if self.ladder_r(self.x, self.y):
                            self.x += 16
                            self.y -= 16
                #To go down to the right with the ladder
                if self.ladder_l(self.x, self.y + 16):
                    for i in range(16):
                        self.pos_counter = 0
                        if self.ladder_l(self.x, self.y + 16):
                            self.x += 16
                            self.y += 16
            # MOVEMENT CHARACTERISTICS FOR THE LEFT
            else:
                # To make the lemming fall with the umbrella:
                if self.umbrella(self.x, self.y) and self.ground(self.x, self.y + 16):
                    self.y += 16
                    self.umbrella_state = True
                elif self.ground(self.x, self.y + 16) and self.umbrella_state:
                    self.y += 16
                    if not self.ground(self.x, self.y + 16):
                        self.umbrella_state = False
                elif self.ground(self.x, self.y + 16) and not self.umbrella_state:
                    self.y += 16
                    self.pos_counter += 1
                    if self.pos_counter > 1:
                        del (l_lemmingsU[i])
                # To move it to the left when the next cell isn't a block
                if not self.ground(self.x, self.y + 16) and self.ground(self.x - 16, self.y):
                    self.x -= 16
                # To change direction if the next cell is a block
                if not self.ground(self.x - 16, self.y):
                    self.direct = 1
                #To save the lemmings
                if self.exit(self.x + 16, self.y):
                    del (l_lemmingsU[i])
                #To go up to the left with the ladder
                if self.ladder_l(self.x, self.y):
                    for i in range(16):
                        if self.ladder_l(self.x, self.y):
                            self.x -= 16
                            self.y -= 16
                #To go down to the left with the ladder
                if self.ladder_r(self.x, self.y + 16):
                    for i in range(16):
                        if self.ladder_r(self.x, self.y + 16):
                            self.x -= 16
                            self.y += 16
        else:
            del (l_lemmingsU[i])

    def draw(self, l_lemmingsD, i):
        if self.x > 256 and self.y > 256:
            del (l_lemmingsD[i])

        elif self.pos_counter > 0:
            pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16, colkey=0)
            del (l_lemmingsD[i])
        else:
            pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16, colkey=0)
