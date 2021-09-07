size = 20
memorization = []
for i in range(0, size+1):
    memorization.append([])
    for j in range(0, size+1):
        memorization[i].append(-1)

def move(R, D, Rm, Dm):
    routes = 0
    if(memorization[D][R] != -1):
        return memorization[D][R]
    else:
        if(R < Rm):
            routes = routes + move(R+1, D, Rm, Dm)
        if(D < Dm):
            routes = routes + move(R, D+1, Rm, Dm)
        if(R == Rm and D == Dm):
            routes = routes + 1
        memorization[D][R] = routes
        return routes

print("Working...")
print(move(0, 0, size, size))
