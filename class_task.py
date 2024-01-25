class Image:
    def __init__(self, resoluton, title, extension):
        self.resolution = resoluton
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def __str__(self):
        return f"{self.title}.{self.extension}"


dogs = Image('6x4', 'Dogs', 'jpg')
book = Image('3x4', 'Book', 'pdf')
car = Image('1920x1080', 'Red car', 'rtf')

dogs.resize('3x4')
print(dogs.resolution, dogs.title, dogs.extension)


book.resize('1920x1080')
print(book.resolution, book.title, book.extension)

car.resize('6x4')
print(car.resolution, car.title, car.extension)

print(car)


class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_str(first, second):
        return f"{first} {second}"
    

greeting = Comment("Hello world")

first_m = Comment.merge_str('Green', 'apple')
print(first_m)

second_m = greeting.merge_str('Hi', 'ok')
print(second_m)


class Comment:
    total_comments = 0

    def __init__(self, text):
        self.text = text
        Comment.total_comments += 1


first_comment = Comment("My first comment")

print(first_comment.text)
print(first_comment.total_comments)
print(Comment.total_comments)
Comment.total_comments = 10
print(Comment.total_comments)
print(first_comment.total_comments)



class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def full_info(name, max_speed, mileage):
        return f"{name}, {max_speed}, {mileage} milles"
bus = Vehicle('Name: Green bus', 'Speed: 100', 'Mileage: 10')

print(Vehicle.full_info('Green bus', '100 km/h', 10))
print(bus.name, bus.max_speed, bus.mileage, end=' ')




class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage





