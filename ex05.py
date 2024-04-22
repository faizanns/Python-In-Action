package_w = [5, 12, 10, 2, 14, 8, 20, 18]#1
print(package_w)

package_w.append(25)#2
print(package_w)

del package_w[2:6] #3
print(package_w)

package_w = sorted(package_w, reverse=True) #4
print(package_w)

package_w = sorted(package_w, reverse=False) #5
print(package_w)

names = ["Bob","Maria", "Doro", "Prof. Turtle", "Asmee"] #6
print(names)
z = zip(names, package_w)
for i in z:
    print(i)

z = zip(names, package_w) #7
for i in z:
    if i[0] == "Prof. Turtle":
        print(i[1])
        break

z = zip(names, package_w) #8
d = dict(z)
print(d.get("Prof. Turtle"))

if d.get("Adam"):         #9
    print("did not shipped")
else:
    print("shipped")

#10
package_w = [i * 1000 if (len(str(i)) == 1) else i for i in package_w]
for z in package_w:
    print(z)

#11
z = zip(names, package_w)
d = dict(z)
for key, value in d.items():
    print(key, ":", value)

#Sort
lst = input("Enter numbers to sort separated by commas only: ")
x = lst.split(",")
x = [round(float(i)) for i in x]
print("Input list: " + str(x))

for i in range(len(x)):
    for j in range(i+1):
        if (x[j] > x[i]):
            swap = x[i]
            x[i] = x[j]
            x[j] = swap
print("Sorted list: " + str(x))

#Pythagoras
p = [(a, b, c) for a in range(1, 101) for b in range(a, 101) for c in range(b + 1, 101) if a**2 + b**2 == c**2]

for i in p:
    print(i)