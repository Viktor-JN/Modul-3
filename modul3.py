svar=input("Repetition 10 ggr:\n")
x=1
while x < 10:
    print(svar)
    x+=1
for x in range(1, 11):
    print(x)
y = int(input("Printa alla tal mellan 1 till \n:"))
y+=1
for x in range(1, y):
    print(x)
z=int(input("Vilka tabeller vill du se, 1 till \n:"))
z+=1
for table in range(1, z):
    print("Tabell", table)
    for x in range(1,z):
        print(table, "*", x, "=", x*table)