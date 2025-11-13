class Rombus:
    def __init__(self, side_a: float | int, angle_a: float | int):
        self.side_a = side_a
        self.angle_a = angle_a
        object.__setattr__(self, 'angle_b', 180 - angle_a)

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                raise ValueError("The value of side side_a must be greater than 0.")


        elif key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("angle_a should be between 0,1 and 179,9.")


        elif key == "angle_b":
            raise ValueError("angle_b is calculated automatically.")


        super().__setattr__(key, value)


    def __str__(self):
        return f"Rombus: side a = {self.side_a}, angle a = {self.angle_a}, angle b = {self.angle_b}"


# rombus_1 = Rombus(side_a=20, angle_a=10)
# print(rombus_1)
#
# rombus_2 = Rombus(side_a=20, angle_a=180)
# print(rombus_2)