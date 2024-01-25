class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")

bmw = Car()

bmw.move()
bmw.stop()


class IT:
    def code(self):
        print("False")
    
    def be_lazy(self):
        print("false")

it_developer = IT()
gamer = IT()

IT.be_lazy(gamer)



class Comment:
    def __init__(self, text, initial_votes_qty=0):
        self.text = text
        self.votes_qty = initial_votes_qty
    
    def upvote(self, qty):
        self.votes_qty += qty


first_comment = Comment("1st message")
print(first_comment.votes_qty)
first_comment.upvote(5)
print(first_comment.votes_qty)
first_comment.upvote(8)
print(first_comment.votes_qty)