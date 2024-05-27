
def contalpha(n, start_char='A'):
    # Convert start_char to its ASCII value
    num = ord(start_char)
    
    # Loop to create the pattern
    for i in range(n):
        for j in range(i + 1):
            # Convert the ASCII value back to character
            ch = chr(num)
            print(ch, end=" ")
            num += 1
        print()  # New line after each row

# Get input from user for the number of rows
n = int(input("Enter the number of rows: "))
contalpha(n)
