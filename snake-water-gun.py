import random
l=['s','w','g']
c=0
p=0
for i in range(10):
    ci=random.choice(l)
    print("choose any s/w/g")
    pi=input()
    if ci=="s" and pi=="w":
        c+=1.
    if pi=="s" and ci=="w":
        p+=1
    if ci=="w" and pi=="g":
        p+=1
    if pi=="w" and ci=="g":
        c+=1
    if ci=="s" and pi=="g":
        p+=1
    if ci=="g" and pi=="w":
        c+=1
    if ci==pi:
        pass
print(f"computer score {c}")
print(f"player score {p}")
if c>p:
    print("Winner is computer")
if p>c:
    print("winner is player1")

