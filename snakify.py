
from math import pow
n = int(input("Num   "))
num = 2
i = 0
while i > -1:
    power = pow(num, i)
    if power > n:
        i -= 1
        print(i, pow(num, i), end=' ')
        break
    i += 1



n = int(input("Num   "))
two_in_power = 2
power = 1

while two_in_power <= n:
    two_in_power *= 2
    power += 1

print(power - 1, two_in_power / 2)




n = int(input())
f0 = 0
f1 = 1
list = []
if n == 0:
    index = 0
elif n == 1:
    index = "1 and 2"

for i in range(2, n):
    f_next = f0 + f1
    if n == f_next:
        print(i)
        list.append(n)
    f0, f1 = f1, f_next
if n not in list:
    print(-1)


from sys import getsizeof  
my_tuple = (2, 5, 7)

gen = (num * num for num in range(100000000))
print(getsizeof(gen))
for elem in gen:
    print(elem)
    if elem == 100:
        break
new_list = [num * num for num in range(100000000)]
print(getsizeof(new_list))

elem = int(input())
i = 0
list = []
while elem != 0:
    i = elem
    elem = int(input())
    if i == elem:
        list.append(i)
        list.append(elem)
print(len(list))
 
elem = int(input())
prev = 0
count = 1
count_list = []
while elem != 0:
    prev = elem
    elem = int(input())
    if prev == elem:
        while prev == elem:
            count += 1
        count_list.append(count)
print(max(count_list))


class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0


    def upvote(self):
        self.votes_qty += 1

    def __add__(first, second):
        return (f"{first.text} {second.text}", first.votes_qty + second.votes_qty)

    def compared_comments(first, second):
        if first.text == second.text and first.votes_qty == second.votes_qty:
            print("True")
        else:
            print("False")


first_comment = Comment("First comment")
first_comment.upvote()
second_comment = Comment("Second comment")
second_comment.upvote()
second_comment.upvote()


print(first_comment + second_comment)
print(Comment.compared_comments(first_comment, second_comment))