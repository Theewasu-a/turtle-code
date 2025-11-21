import turtle
import random

class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()

        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)

        turtle.penup()


class ArtController:

    def __init__(self):
        turtle.bgcolor("black")
        turtle.speed(0)
        turtle.colormode(255)
        turtle.tracer(0)

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def random_location(self):
        return [random.randint(-300,300),
                random.randint(-250,250)]

    def draw_single_polygon(self, sides):
        size = random.randint(50, 150)
        angle = random.randint(0, 90)
        color = self.get_new_color()
        border = random.randint(1, 10)
        location = [random.randint(-300, 300), random.randint(-200, 200)]

        Polygon(sides, size, angle, location, color, border).draw()

    def art1(self):  
        for _ in range(20):
            self.draw_single_polygon(3)

    def art2(self):  
        for _ in range(20):
            self.draw_single_polygon(4)

    def art3(self):  
        for _ in range(20):
            self.draw_single_polygon(5)

    def art4(self):  
        for _ in range(20):
            self.draw_single_polygon(random.choice([3,4,5]))

    def art5(self):
        for _ in range(20):
            base_size = random.randint(50, 140)
            loc = self.random_location()
            angle = random.randint(0, 360)
            col = self.get_new_color()

            layers = random.randint(3, 5)

            size = base_size
            for i in range(layers):
                border = 3 if i == 0 else 1    
                Polygon(3, size, angle, loc, col, border).draw()
                size *= 0.70                    
                angle += random.randint(-10, 10)

    def art6(self):
        for _ in range(20):
            base_size = random.randint(60, 150)
            loc = self.random_location()
            angle = random.randint(0, 360)
            col = self.get_new_color()

            layers = random.randint(4, 6)  

            size = base_size
            for i in range(layers):
                border = 3 if i == 0 else 1 
                Polygon(4, size, angle, loc, col, border).draw()

                size *= 0.70               
                angle += random.randint(-12, 12)  

    def art7(self):
        for _ in range(20):
            base_size = random.randint(60, 150)
            loc = self.random_location()
            angle = random.randint(0, 360)
            col = self.get_new_color()

            layers = random.randint(4, 6)

            size = base_size
            for i in range(layers):
                border = 3 if i == 0 else 1
                Polygon(5, size, angle, loc, col, border).draw()

                size *= 0.70
                angle += random.randint(-12, 12)

    def art8(self):
        for _ in range(20):
            sides = random.choice([3, 4, 5])
            base_size = random.randint(60, 150)
            loc = self.random_location()
            angle = random.randint(0, 360)
            col = self.get_new_color()

            layers = random.randint(4, 6)

            size = base_size
            for i in range(layers):
                border = 3 if i == 0 else 1
                Polygon(sides, size, angle, loc, col, border).draw()
                size *= 0.70
                angle += random.randint(-12, 12)

    def art9(self):
        for _ in range(20):
            sides = random.choice([3, 4, 5])
            size = random.randint(40, 140)
            loc = self.random_location()
            angle = random.randint(0, 360)
            col = self.get_new_color()
            border = random.randint(1, 5)
            for _ in range(random.randint(0,5)):
                Polygon(sides, size, angle, loc, col, border).draw()
                size *= 0.7
                angle += random.randint(-12, 12)



def main():
    choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
    art = ArtController()

    if   choice == 1: art.art1()
    elif choice == 2: art.art2()
    elif choice == 3: art.art3()
    elif choice == 4: art.art4()
    elif choice == 5: art.art5()
    elif choice == 6: art.art6()
    elif choice == 7: art.art7()
    elif choice == 8: art.art8()
    elif choice == 9: art.art9()
    else:
        print("Invalid selection.")
        return

    turtle.update()
    turtle.done()

if __name__ == "__main__":
    main()