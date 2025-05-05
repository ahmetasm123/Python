x=int(input("how many eg: "))
if 100<x<150:
    y=x%12
    t=y%6
    f=y//6
    z=x//12
    print("6 pack eg= "+str(f))
    print("12 pack eg= "+str(z))
    print("eat "+str(t)+" eg")
elif x<100:
    print("weak")
elif x>150:
    print("you're not him")