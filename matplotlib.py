import sys
import matplotlib.pyplot as plt

plt.xlabel("Coordinates X")
plt.ylabel("Coordinates Y")
plt.xlim()
plt.ylim()
plt.show()

coordinatesx = []
coordinatesy = []

print("1.Input Coordinates")
print("2.Show")
print("3.Erase")
print("4.Exit")

draw = 1
while draw == 1:
    choose = int(input("Choose:"))
    if choose == 1:
        x = eval(input("Input Coordinates x:"))  # Input Coordinates X
        coordinatesx.append(x)
        y = eval(input("Input Coordinates y:"))  # Input Coordinates Y
        coordinatesy.append(y)

    elif choose == 2:
        if len(coordinatesx) == 0:
            plt.xlim()
            plt.ylim()
            plt.show()
        else:
            for i in range(len(coordinatesx)):
                plt.plot(coordinatesx[i], coordinatesy[i])
                plt.show()

    elif choose == 3:
        coordinatesx.clear()
        coordinatesy.clear()
        break

    elif choose == 4:
        sys.exit("Exit")
