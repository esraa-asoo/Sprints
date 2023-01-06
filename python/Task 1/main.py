# Approach 1 : Convert the string to a list and then change the value.
# Input Format
# The first line contains a string.
# The next line contains an integer , denoting the index location and a character separated by a space.

'''
def change_string(string, position, character):
    lis = list(string)
    lis[position] = character
    return (print("".join(lis)))

if __name__ == '__main__':
    string = input("Enter the String: ")
    index, char = input("Enter index of the character you want to change (start from 0),and \n enter the new caracter: ").split()
    result = change_string(string,int(index),char)
'''

'''
# Sample Input:
    Enter the String: EsraaarafaAhmed
    Enter index of the character you want to change (start from 0),and 
    enter the new caracter:5 A
    
# Sample Output   
    EsraaArafaAhmed
'''

# Approach 2 : Slice the string and join it back.
# Input Format
# The first line contains a string.
# The next line contains an integer, denoting the index location and a character separated by a space.
def change_string(string, position, character):
    return str[:int(i)]+char+str[int(i)+1:]

if __name__ == '__main__':
    str = input("Enter the String: ")
    i, char = input("Enter index of the character you want to change (start from 0),and \n enter the new caracter:").split()
    new_char = change_string(str, int(i), char)
    print(new_char)


'''
# Sample Input:
    Enter the String: EsraaarafaAhmed
    Enter index of the character you want to change (start from 0),and 
    enter the new caracter:5 A
    
 Output:   
    EsraaArafaAhmed
'''
