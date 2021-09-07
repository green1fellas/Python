import winsound

size = 20
routes = 0

def move(R, D, Rm, Dm):
    global routes

    if(R < Rm):
        move(R+1, D, Rm, Dm)
    if(D < Dm):
        move(R, D+1, Rm, Dm)

    if(R == Rm and D == Dm):
        routes = routes + 1

print("Working...")
move(0, 0, size, size)
print(routes)
winsound.Beep(1000, 500)
    