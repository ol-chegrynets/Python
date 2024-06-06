def reading(file):
    #print(file)
    filename = f'{file}'
    with open(filename) as file:
        c = file.read()
    return c.split(" ")

b = reading("suit.txt")
print(b)




"""filename = 'suit.txt'
with open(filename) as file:
    c = file.read()
    a = c.split(" ")
print(a)"""

"""def pretty_print(text, dash="#"):
    new_text = f"{dash} {text} {dash}"
    line_size = len(new_text)
    horizontal_line = dash * line_size

    # Replace lines to create and return new string
    print(horizontal_line)
    print(new_text)
    print(horizontal_line)

    # return <your solution here>


# print(pretty_print("Python is not a snake", '/'))"""
"""card_suit = open('suit.txt', 'r')
.close()
print(card_suit)
"""