
# Asks user to enter date while program outputs whether that day is a holiday or a regular working day.
month = int(input("Enter an month as an integer from 1-12: ")) # input month
if (month>12) or (0>=month): # only 12 months
    print ("Invalid input. Months are numbered from 1 to 12")
else:
    date = int(input("Enter a date from 1-31: ")) # input date
    if (date>31) or (0>=date): # no month has more than 31 days
        print ("Invalid input. No month has more than 31 days/less than 0 days")
    elif ((month==4) or (month==6) or (month==9) or (month==11)) and (date>30):
        print ("Invalid input. Input month does not have more than 30 days")
        # These months only have 30 days
    elif (month==2) and (date>28): # Feb only has 28 days
        print ("Invalid input. February only has 28 days")
    elif (month==9) and (date==2): # Labor day
        print ("September 9th is Labor Day")
    elif (month==9) and ((1==date) or (2<date<30)): # No holidays in Sept
        print ("September",date,"is not a holiday")
    elif (month==10) and (date==15): # Fall break
        print ("October",date,"is part of fall break")
    elif (month==10) and (date==16):# Fall break and Eid
        print ("October",date,"is part of fall break")
        print ("October",date,"is also Eid ul Adha")
    elif (month==10) and ((1<=date<15) or (16<date<=31)): # No holidays in Oct
        print ("October",date,"is not a holiday")
    elif (month==11) and (28<=date<=29): # Thanksgiving break
        print ("November",date,"is part of Thanksgiving break")
    elif (month==11) and (1<=date<28 or date==30): # No holidays in Nov
        print ("November",date,"is not a holiday")
    elif (month==12) and (21<=date<=31): # Winter break
        print ("December",date,"is part of winter recess")
    elif (month==12) and (1<=date<21): # No holidays in Dec
        print ("December",date, "is not a holiday")
    elif (month==1) and ((1<=date<20) or (20<date<=26)): # Winter break in Jan
        print("January",date,"is part of winter recess")
    elif (month==1) and (date==20): # Winter break and MLK day
        print ("January",date,"is part of winter recess")
        print ("January",date,"is also Martin Luter King Day")
    elif (month==1) and (26<date<=31): # No holidays in Jan
        print ("January",date,"is not part of a holiday")
    elif (month==2) and (date==17): # President's day and my bday
        print ("February",date,"is President's day")
        print ("February",date,"is also Sana's birthday")
    elif (month==2) and ((1<=date<17) or (17<date<=28)): # No holidays in Feb
        print ("February",date,"is not a holiday")
    elif (month==3) and (17<=date<=23): # Spring break
        print ("March",date,"is part of spring break")
    elif (month==3) and ((1<=date<17) or (23<date<=31)): # No holidays in Mar
        print ("March",date,"is not part of a holiday")
    elif (month==4) and (1<=date<=30): # No holidays in April
        print ("April",date,"is not part of a holiday")
    elif (month==5) and (date==28): # Memorial day
        print ("May",date,"is Memorial Day")
    elif (month==5) and (date!=28): # No holidays in May
        print ("May",date,"is not part of a holiday")
    elif (month==6) and (date==29): # First day of Ramadan
        print ("June",date, "is the first day of Ramadan")
    elif (month==6) and (date!=29): # No holidays in June
        print ("June",date,"is not part of a holiday")
    elif (month==7) and (date==4): # Independence day
        print ("July",date,"is Independence Day")
    elif (month==7) and ((1<=date<4) or (4<date<28) or (28<date<=31)):
        print ("July",date,"is not part of a holiday") # No holidays in July
    elif (month==8) and (1<=date<=31): # No holidays in Aug
        print ("August",date,"is not part of a holiday")
        


    
