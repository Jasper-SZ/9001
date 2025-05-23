class Player:
    def __init__(self):
        self.health = 2
        self.num_medicine = 0
        self.num_hammer = 0
        self.num_compass = 0
        self.x = 0
        self.y = 0
    
    def is_out_of_health(self):
        if self.health == 0:
            return True
        else:
            return False
    
    def use_medicine(self):
        self.num_medicine -= 1
        self.health += self.health
    
    def use_hammer(self,x,y,grip):
        grip[x][y] = '.'
        self.num_hammer -= 1

    def use_compass(self,x ,y,grip):
        self.num_compass -=1
        print(f"It is {grip[x][y]} there.")

    def add_medicine(self):
        self.num_medicine += 1

    def add_hammer(self):
        self.num_hammer += 1

    def add_compass(self):
        self.num_compass += 1
    
    def bomb(self):
        self.health -= 1

    def move(self, x, y,grip, default_grip):
        symbol = grip[x][y]
        if symbol == '.':
            while 1:
                order = input("Do you want to use medicine or compass(compass/medicine/N)?")
                if order != 'medicine' and order != 'compass' and order != 'N':
                    print("Invalid response!")
                elif order == 'compass':
                    if self.num_compass == 0:
                        print("You do not have a compass.")
                    else:
                        while 1:
                            s = input("Which direction do you want to check?(N/S/E/W)")
                            if s != 'N' and s != 'S' and s != 'E' and s != 'W':
                                print("Invalid direction!")
                            elif s == 'N':
                                if (x - 1) < 0:
                                    print("You have reached the northernmost.")
                                else:
                                    self.use_compass(x-1, y, grip)
                                    default_grip[x-1][y] = grip[x-1][y]
                                    break
                            elif s == 'S':
                                if (x + 1) >5:
                                    print("You have reached the southernmost.")
                                else:
                                    self.use_compass(x+1, y, grip)
                                    default_grip[x+1][y] = grip[x+1][y]
                                    break
                            elif s == 'E':
                                if (y + 1) > 5:
                                    print("You have reached the easternmost.")
                                else:
                                    self.use_compass(x, y+1, grip)
                                    default_grip[x][y+1] = grip[x][y+1]
                                    break
                            else:
                                if (y - 1) < 0:
                                    print("You have reached the westernmost.")
                                else:
                                    self.use_compass(x, y-1, grip)
                                    default_grip[x][y-1] = grip[x][y-1]
                                    break
                        break
                elif order == 'medicine':
                    if self.num_medicine == 0:
                        print("You do not have medicine.")
                    else:
                        self.use_medicine()
                        print(f"Your current health is {self.health}.")
                        break
                else:
                    break
            self.x = x
            self.y = y
            return True
        elif symbol == '*':
            if self.num_hammer != 0:
                while 1:
                    answer = input("Do you want to crash this wall?(Y/N)")
                    if answer != 'Y' and answer != 'N':
                        print("Invalid answer.")
                    elif answer == 'Y':
                        self.use_hammer(x, y, grip)
                        self.x = x
                        self.y = y
                        return True
                    else:
                        return False
            else:
                print("You just hit a wall and you do not have a hammer.")
                return False
        elif symbol == 'B':
            print("You have stepped on the bomb. Health -1.")
            self.bomb()
            if self.is_out_of_health():
                if self.num_medicine > 0:
                    self.use_medicine()
                    print("Medicine automatically used.")
                else:
                    print("Health is 0.")
                return True
            else:
                while 1:
                    order = input("Do you want to use medicine or compass(compass/medicine/N)?")
                    if order != 'medicine' and order != 'compass' and order != 'N':
                        print("Invalid response!")
                    elif order == 'compass':
                        if self.num_compass == 0:
                            print("You do not have a compass.")
                        else:
                            while 1:
                                s = input("Which direction do you want to check?(N/S/E/W)")
                                if s != 'N' and s != 'S' and s != 'E' and s != 'W':
                                    print("Invalid direction!")
                                elif s == 'N':
                                    if (x - 1) < 0:
                                        print("You have reached the northernmost.")
                                    else:
                                        self.use_compass(x-1, y, grip)
                                        break
                                elif s == 'S':
                                    if (x + 1) >5:
                                        print("You have reached the southernmost.")
                                    else:
                                        self.use_compass(x+1, y, grip)
                                        break
                                elif s == 'E':
                                    if (y + 1) > 5:
                                        print("You have reached the easternmost.")
                                    else:
                                        self.use_compass(x, y+1, grip)
                                        break
                                else:
                                    if (y - 1) < 0:
                                        print("You have reached the westernmost.")
                                    else:
                                        self.use_compass(x, y-1, grip)
                                        break
                            break
                    elif order == 'medicine':
                        if self.num_medicine == 0:
                            print("You do not have medicine.")
                        else:
                            self.use_medicine()
                            print(f"Your current health is {self.health}.")
                            break
                    else:
                        break
            self.x = x
            self.y = y
            return True
        elif symbol == 'M':
            print("You got a medicine!")
            self.add_medicine()
            self.x = x
            self.y = y
            return True
        elif symbol == 'C':
            print("You got a compass!")
            self.add_compass()
            self.x = x
            self.y = y
            return True
        elif symbol == 'H':
            print("You got a hammer!")
            self.add_hammer()
            self.x = x
            self.y = y
            return True
        elif symbol == 'T':
            self.x = x
            self.y = y
            #print("Congratulations! You win!")
            return True
    
    def display_status(self):
        print(f"Health:   {self.health}")
        print(f"Medicine: {self.num_medicine}")
        print(f"Hammer:   {self.num_hammer}")
        print(f"Compass:  {self.num_compass}")
        
                    

        
        


