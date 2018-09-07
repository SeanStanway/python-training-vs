def print_function(exampleName, content):
    print('{} {}'.format(exampleName, content))
def newLine():
    print('')

def my_function():
    a = 2
    return a
print_function("Function:", my_function())

newLine()

b = 5
c = 7
if b > c:
    print_function('If Statement:', 'b is more than c')
else:
    print_function('If Statement:','c is more than b')

newLine()
