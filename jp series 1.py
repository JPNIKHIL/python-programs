s = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))
o = input("Enter 'horizontal' or 'vertical': ")
order = input("Enter 'forward' or 'reverse': ")
if order == 'forward':
    if o == 'horizontal':
        print(" ".join(str(i) for i in range(s, end + 1)))
    elif o == 'vertical':
        for i in range(s, end + 1):
            print(i)
    else:
        print("Invalid orientation choice. Please enter 'horizontal' or 'vertical'.")

elif order == 'reverse':
    if o == 'horizontal':
        print(" ".join(str(i) for i in range(end, s - 1, -1)))
    elif o == 'vertical':
        for i in range(end, start - 1, -1):
            print(i)
    else:
        print("Invalid orientation choice. Please enter 'horizontal' or 'vertical'.")

else:
    print("Invalid order choice. Please enter 'forward' or 'reverse'.")
