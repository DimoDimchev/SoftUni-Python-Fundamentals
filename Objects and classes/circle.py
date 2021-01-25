class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def calculate_circumference(self):
        circumference = Circle.__pi * 2 * self.radius
        return circumference

    def calculate_area(self):
        area = Circle.__pi * (self.radius ** 2)
        return area

    def calculate_area_of_sector(self, angle):
        area_of_sector = ((angle / 360) * (self.radius ** 2)) * Circle.__pi
        return area_of_sector
