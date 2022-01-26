class Car:
    # dunder init method. set a current_speed and max_speed attribute
    def __init__(self, current_speed = 0, max_speed = 100):
        self.__current_speed = current_speed
        self.max_speed = max_speed
    # implement the following methods:

    # accelerate
    # brake

    def accelerate(self, speed_increase):
        ## add the increase on to the current speed

        # if self.__current_speed + speed_increase < self.max_speed:
        #     self.__current_speed += speed_increase
        # else:
        #     self.__current_speed = self.max_speed
        
        self.__current_speed = min(self.max_speed, self.__current_speed + speed_increase)


    def decelerate(self, speed_decrease):
        
        # if self.__current_speed >= speed_decrease:
        #     self.__current_speed -= speed_decrease
        # else:
        #     self.__current_speed = 0

        self.__current_speed = max(0, self.__current_speed - speed_decrease)

    def get_speed(self):
        return self.__current_speed

variable = 1

if __name__ == '__main__':
    bugatti = Car(70, 400)
    print(bugatti.get_speed())

    bugatti.accelerate(10)
    print(bugatti.get_speed())

    bugatti.decelerate(40)
    print(bugatti.get_speed())