num1 = []
num2 = []
opt = []
output = []
m = 0
while m <= 0:
    x = float(input("Enter First Number: "))
    num1.append(str(x))
    y = float(input("Enter Second Number: "))
    num2.append(str(y))
    z = raw_input("Enter The Operator(+,-,*,/): ")
    if z == "+":
        print "result: " + str(x + y)
        output.append(str(x + y))
        opt.append(z)
    elif z == "-":
        print "result: " + str(x - y)
        output.append(str(x - y))
        opt.append(z)
    elif z == "*":
        print "result: " + str(x * y)
        output.append(str(x * y))
        opt.append(z)
    elif z == "/":
        print "result: " + str(x / y)
        output.append(str(x / y))
        opt.append(z)
    k = raw_input("\nPress Enter to continue or Press 'n' to exit: ")
    if k == "n":
        break
    print"\n"
print "Results:" + "\n".join(num1) + " ".join(opt) + " ".join(num2) + "=".join(output)
