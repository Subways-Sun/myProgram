def group(numberOfGroups):
    import random
    name=input("Please enter the name of students (separate using comma): ").split(",") 
    totalNumber=len(name)
    baseNumber=totalNumber//numberOfGroups
    extraNumber=totalNumber%numberOfGroups
    for i in range(numberOfGroups):
        group=[]
        if extraNumber>0:
            for j in range(baseNumber+1):
                a=random.choice(name)
                name.remove(a)
                group.append(a)
        else:
            for j in range(baseNumber):
                a=random.choice(name)
                name.remove(a)
                group.append(a)
        extraNumber-=1
        print("Students of group {0}: {1}".format(i+1,group))
