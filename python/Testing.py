import time



string = "characters"

# Displays individual characters from given string
print("Individual characters from given string:")

# Iterate through the string and display individual character
for i in range(0, len(string)):
    time.sleep(0.09)
    print(string[i], end="  ")
