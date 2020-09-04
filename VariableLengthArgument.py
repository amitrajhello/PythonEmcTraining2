# variable length argument parameter
def demo(*args):
    print(args)


# demo()
# demo(1, 2, 3, 4, 'five')

items = [11, 22, 33]
demo(items)
demo([items[0], items[1], items[2]])
demo(*items)  # passing the content of the object as an argument

demo('peter')
demo(*'peter')

