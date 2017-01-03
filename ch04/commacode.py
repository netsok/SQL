# Create a function which turns a list into a string
# and returns the string.
def listing(var):
    string = var[0]
    for i in range(1, len(var)-1):
        string = string + ', ' + var[i]
    
    string = string + ', and ' + var[len(var)-1]
    print(string)

# Create a list.
spam = ['apples', 'bananas', 'tofu', 'cats']

# Call the defined function on the list.
listing(spam)
