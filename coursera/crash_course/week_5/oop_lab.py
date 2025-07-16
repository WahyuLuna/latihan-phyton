class Elevator:

    def __init__(self, bottom, top, current):
        self.bottom = bottom
        self.top = top
        self.current = current
        pass
    def up(self):
        if self.current <10:
            self.current += 1
        pass
    def down(self):
        if self.current > -1:
            self.current -= 1
        pass
    def go_to(self, floor):
        self.floor = floor
        self.current = self.floor
        pass
    
    def __str__(self):
        return "Current floor: {}".format(self.current)

elevator = Elevator(-1, 10, 0)
elevator.up() 
print(elevator) #should output 1
elevator.down() 
print(elevator) #should output 0
elevator.go_to(10) 
print(elevator) #should output 10
# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1
elevator.go_to(5)
print(elevator)