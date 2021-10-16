import random
import time
import numpy as np

class Board():

    random_co_y = random.randrange(0, 8)
    random_co_x = random.randrange(0, 8)
    chessBord = np.zeros((8, 8), dtype=int)
    steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    def printBoard(self):
        print(self.chessBord)


    def randomChoice(self):

        while True:

            random_choice = random.randrange(0, 8)
            #print("random_choice: " + str(random_choice))

            if self.horseMove(self.steps[random_choice]):
                continue
        
            success = False  
            random_steps = random.shuffle(self.steps)  
            print(random_steps)
            for step in self.steps:
                success = self.horseMove(step)
                if success == False:
                    continue
                else:
                    break
            
            if success == False:
                print("End")
                break

    def go(self, pair):
        self.chessBord[self.random_co_y, self.random_co_x] = 1
        self.random_co_y = self.random_co_y + pair[0]
        self.random_co_x = self.random_co_x + pair[1]
        self.chessBord[self.random_co_y, self.random_co_x] = 7
                
    def horseMove(self, pair):

        if pair[0] < 0 and pair[1] < 0:
            if self.random_co_y + pair[0] >= 0 and self.random_co_x + pair[1] >= 0:
                future_cor = self.chessBord[self.random_co_y + pair[0], self.random_co_x + pair[1]]
                if future_cor == 0:
                    self.go(pair)
                    self.printBoard()
                    print()
                    time.sleep(1)
                    return True
        
        if pair[0] > 0 and pair[1] < 0: 
            if self.random_co_y + pair[0] <= 7 and self.random_co_x + pair[1] >= 0:
                future_cor = self.chessBord[self.random_co_y + pair[0], self.random_co_x + pair[1]]
                if future_cor == 0:
                    self.go(pair)
                    self.printBoard()
                    print()
                    time.sleep(1)
                    return True

        if pair[0] < 0 and pair[1] > 0:
            if self.random_co_y + pair[0] >= 0 and self.random_co_x + pair[1] <= 7:
                future_cor = self.chessBord[self.random_co_y + pair[0], self.random_co_x + pair[1]]
                if future_cor == 0:
                    self.go(pair)
                    self.printBoard()
                    print()
                    time.sleep(1)
                    return True

        if pair[0] > 0 and pair[1] > 0:
            if self.random_co_y + pair[0] <= 7 and self.random_co_x + pair[1] <= 7:
                future_cor = self.chessBord[self.random_co_y + pair[0], self.random_co_x + pair[1]]
                if future_cor == 0:
                    self.go(pair)
                    self.printBoard()
                    print()
                    time.sleep(1)
                    return True
        
        return False

object = Board()
object.randomChoice()