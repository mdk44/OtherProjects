def new_card():
    colors = ['Red', 'Yellow', 'Blue', 'Green', 'White', 'Rainbow']
    # colors = ['Red', 'Yellow', 'Blue', 'Green', 'White']
    numbers = [1, 2, 3, 4, 5]
    return colors, numbers

def print_hand():
    for i in range(1, 6):
        print("Card " + str(i) + ":", cards[i])

def hint_number(x, num):
    for y in range(1, 6):
        if y in x:
            colors = cards[y][0]
            numbers = [num]
            cards[y] = colors, numbers
        else:
            if num in cards[y][1]:
                cards[y][1].remove(num)
    return True

def hint_color(x, color):
    for y in range(1, 6):
        if y in x:
            colors = [color]
            numbers = cards[y][1]
            cards[y] = colors, numbers
        else:
            if color in cards[y][0]:
                cards[y][0].remove(color)
    return True

def discard(num):
    for i in range(num + 1, 6):
        cards[i - 1] = cards[i]
    cards[5] = new_card()
    return True

def play(num):
    for i in range(num + 1, 6):
        cards[i - 1] = cards[i]
    cards[5] = new_card()
    return True

cards = dict()
cards[1] = new_card()
cards[2] = new_card()
cards[3] = new_card()
cards[4] = new_card()
cards[5] = new_card()

hint_number([2,5], 1)
hint_color([5], 'Green')
play(5)
hint_color([2], 'White')
play(2)
hint_number([5], 1)


print_hand()