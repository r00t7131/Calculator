output = []
m = 0
while m <= 0:
    x = float(input("Enter First Number: "))
    y = float(input("Enter Second Number: "))
    z = raw_input("Enter The Operator(+,-,*,/): ")
    if z == "+":
        print "result: " + str(x + y)
        output.append(str(x + y))
    elif z == "-":
        print "result: " + str(x - y)
        output.append(str(x - y))
    elif z == "*":
        print "result: " + str(x * y)
        output.append(str(x * y))
    elif z == "/":
        print "result: " + str(x / y)
        output.append(str(x / y))
    k = raw_input("\nPress Enter to continue or Press 'n' to exit: ")
    if k == "n":
        break
    print"\n"
print "Results: " + ", ".join(output)
