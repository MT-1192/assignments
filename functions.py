'''1.reversing the string using split,reverse and join functions.

original_string = input("Enter the string: ")
split_list = original_string.split()[: : -1]
l = []
for i in split_list:
    l.append(i)
print(" ".join(l))'''


'''2.using join function.
given_string = ("ABBCDEFFGHILJK")
converted_string = list(set(given_string))
converted_string.sort()
required_string = ''.join(converted_string)
print(required_string)'''

'''3.program to print all the positions of sub string in a given string using while loop.'''

def find_substring_position(string,sub_string):
    positions = []
    start_index = 0
    while True:
        index = string.find(sub_string, start_index)
        if index == -1:
            break
        else:
            positions.append(index)
            start_index = index + 1
    return positions
string = input("Enter the string: ")
sub_string = input("Enter the sub string: ")
positions = find_substring_position(string,sub_string)
print(positions)

    

