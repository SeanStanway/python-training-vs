import customFunctions as func

name = input('What is your name?\n')
func.newLine()
func.print_function('Hello', name)

func.newLine()

try:
    x = input('Input desired number to square\n')
    squared_x = x * x
except TypeError as e:
    squared_x = float(x) * float(x)
finally:
    func.print_function('Squared number:' ,squared_x)


func.newLine()

def user_input(message, message_error=None):
    while True:
        try:
            number = float(input(message))
            print(number)
            return
        except ValueError:
            if message_error is not None:
                print(message_error)
            else:
                print('Error')

user_number = user_input('Enter number please: ', 'Number unknown')