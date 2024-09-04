### Problem 874. Walking Robot Simulation
### tags: Array, Hashtable, Simulation
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.x = 0
        self.y = 0
        self.direction = 0
        self.maxDist = 0
        self.obj ={}
        for o in obstacles:
            k = "{},{}".format(o[0], o[1])
            if(k not in self.obj):
                self.obj[k] = 1
        
        # N=0, E=1, S=2, W=3
        def updateLocation(distance):
            if(self.direction & 1 == 1):
                while(distance != 0):
                    newX = 0
                    if(self.direction == 1):
                        newX = self.x + 1
                    else:
                        newX = self.x - 1
                    k = "{},{}".format(newX, self.y)
                    if(k in self.obj):
                        break
                    else:
                        self.x = newX
                        self.maxDist = max(self.maxDist, mdistance(self.x, self.y))
                        distance -= 1
            else:
                while(distance > 0):
                    newY = 0
                    if(self.direction == 0):
                        newY = self.y + 1
                    else:
                        newY = self.y - 1
                    k = "{},{}".format(self.x, newY)
                    if(k in self.obj):
                        break
                    else:
                        self.y = newY
                        self.maxDist = max(self.maxDist, mdistance(self.x, self.y))
                        distance -= 1

        def mdistance(x, y):
            return x * x + y * y

        def updateDirection(isLeft):
            if(isLeft):
                if(self.direction == 0):
                    self.direction = 3
                else:
                    self.direction -= 1
            else:
                # right
                if(self.direction == 3):
                    self.direction = 0
                else:
                    self.direction += 1

        directions = {0: 'N', 1: 'E', 2: 'S' , 3: 'W'}
        for command in commands:
            if(command == -2):
                updateDirection(True)
            elif(command == -1):
                updateDirection(False)
            else:
                updateLocation(command)
            print("facing:" ,directions[self.direction], "position", self.x, self.y)

        return self.maxDist


### Optimized 

class Solution2:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.x = 0
        self.y = 0
        self.direction = 0
        self.maxDist = 0
        self.obj ={}
        for o in obstacles:
            k = "{},{}".format(o[0], o[1])
            if(k not in self.obj):
                self.obj[k] = 1
        # N=0, E=1, S=2, W=3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def updateLocation(distance):
            dx, dy = directions[self.direction]
            while(distance != 0):
                k = "{},{}".format(self.x + dx, self.y + dy)
                if(k in self.obj):
                    break
                else:
                    self.x, self.y = self.x + dx, self.y + dy
                    self.maxDist = max(self.maxDist, mdistance(self.x, self.y))
                    distance -= 1

        def mdistance(x, y):
            return x * x + y * y
        # dn = {0: 'N', 1: 'E', 2: 'S' , 3: 'W'}
        for command in commands:
            if(command == -2):
                self.direction = (self.direction - 1) % 4 
            elif(command == -1):
                self.direction = (self.direction + 1) % 4 
            else:
                updateLocation(command)
            # print("facing:" ,dn[self.direction], "position", self.x, self.y)
        return self.maxDist