h=input("Enter hours:")
if h <=12 and h!=0:
    ap=raw_input("Chosse (am or pm):")
m=input("Enter minutes:")
c=input("want to convert(12 or 24):")
if c==24:
    if h==00:
        hour=00
    elif h<12:
        if ap=="am":
            hour=h
        elif ap=="pm":
            hour=h+12
    elif h>12:
        hour=h
    elif h==12:
        if ap=="am":
            hour=0
        elif ap=="pm":
            hour=h
elif c==12:
    if h==00:
        hour=12,"am"
    elif h<12:
        if ap=="am":
            hour=h,"am"
        elif ap=="pm":
            houre=h-12,"pm"
    elif h==12:
        if ap=="am":
            hour=h,"am"
        elif ap=="pm":
            hour=h,"pm"
    elif h>12:
        hour=h-12,"pm"
print "hour",(hour),":","mints",m