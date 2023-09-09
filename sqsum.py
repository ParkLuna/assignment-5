class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2
x = float(input("Enter the value for x: "))
y = float(input("Enter the value for y: "))
z = float(input("Enter the value for z: "))
point = Point(x, y, z)
result = point.sqSum()
print("Squared Sum:", result)