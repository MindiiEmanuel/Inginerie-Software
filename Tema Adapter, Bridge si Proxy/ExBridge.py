# Implementarea Bridge

# Clasele Implementor definesc interfețe pentru implementările concrete

class DrawingAPIOne:
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at {x}:{y} radius {radius}")


class DrawingAPITwo:
    def draw_circle(self, x, y, radius):
        print(f"API2.circle at {x}:{y} radius {radius}")


# Clasa abstractă din care se vor deriva alte clase

class Shape:
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    def draw(self):
        pass

    def resize(self, radius):
        pass


# Clasele rafinate extind clasa Shape

class CircleShape(Shape):
    def __init__(self, x, y, radius, drawing_api):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def resize(self, radius):
        self.radius = radius


# Utilizarea Bridge

def main():
    shapes = [CircleShape(1, 2, 3, DrawingAPIOne()), CircleShape(5, 7, 11, DrawingAPITwo())]

    for shape in shapes:
        shape.draw()


if __name__ == '__main__':
    main()
