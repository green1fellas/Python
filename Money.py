def Tax():
    return 0.162

def Income(hr, amt):
    return hr*amt

def ReachGoalAmt(amt, tax, goal):
    return round(goal/(1 - tax), 2)

def ReachGoalHr(amt, tax, goal):
    return (str(round(ReachGoalAmt(amt, tax, goal)/amt)) + 
    " hours needed to reach $" + str(goal))

print(ReachGoalHr(25, Tax(), 500))

print(Income(25,25)*(1 -Tax()))
