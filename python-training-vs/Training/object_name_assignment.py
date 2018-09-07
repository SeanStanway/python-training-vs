import customFunctions as func

print('Assigning values: a_name = an_object')
print('An object can have multiple names')
func.newLine()
x = y = [7, 8, 9]
print('Create two names for an object (x, y, for [7, 8, 9] object)')
func.print_function('List 1:', x)
func.print_function('List 2:', y)
print('Assigning the name x a different object does not affect y (e.g. x = [13, 8, 9])')
x = [13, 8, 9]
func.print_function('List 1, assigned new value:', x)
func.print_function('List 2, stays the same:', y)
x = y = [7, 8, 9]
print('Modifying the value will cascade the mutation to names that contain that object (e.g. x[0] = 13)')
x[0] = 13
func.print_function('List 1, modified value:', x)
func.print_function('List 2, mutation cascaded:', y)

