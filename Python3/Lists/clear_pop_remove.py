list = [10, 'heh', 'i\'m a dude', 'he\'s a dude', 'she\'s a dude']
print(list)

last_item = list.pop()
print(list)
print(f'Last item \'{last_item}\' has been popped.')

list.remove(10)
print(list)

list.clear()
print(list)