x = 0
y = 0
a, b = 8, 0

up = 1
right = 2
down = 3
left = 4

direction = right


def move():
    global x, y
    if direction == up:
        y += 1
    elif direction == right:
        x += 1
    elif direction == down:
        y -= 1
    elif direction == left:
        x -= 1


def turn():
    global direction
    if direction == up:
        direction = left
    elif direction == right:
        direction = up
    elif direction == down:
        direction = right
    elif direction == left:
        direction = down


points = []
for i in range(1000):
    move()
    b += 1
    if a == b:
        turn()
        b = 0
        a -= 2
        if a == 0:
            a = 8
    points.append((x, y))

c = 0
last = ()
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if points[i] == points[j]:
            c += 1
            last = points[i]

print(c, last)