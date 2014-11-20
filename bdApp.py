# User inputs two names and two dates - program returns which of the two is older.



# first person's name/bday
name1 = str(input("Enter 1st person's name: "))
bday1 = int(input("Enter 1st person's year of birth year, month, and date: "))
year1 = bday1//10000 # 1st person year
month1 = ((bday1%1000)//100) # 1st person month
date1 = ((bday1%10000000)%100) # 1st person day

print (name1+"'s year of birth: ",year1) # year 1
print (name1+"'s month of birth: ",month1) # print month
print (name1+"'s date of birth: ",date1) # print date
print(name1,"was born on",str(date1)+"/"+str(month1)+"/"+str(year1))
# print names with correct format

# second person's name/bday
name2 = str(input("Enter 2nd person's name: "))
bday2 = int(input("Enter 2nd person's year of birth year, month, and date: "))
year2 = bday2//10000 # 2nd person year
month2 = ((bday2%1000)//100) # 2nd person month
date2 = ((bday2%10000000)%100) # 2nd person day

print (name2+"'s year of birth:",year2) # print year
print (name2+"'s month of birth:",month2) # print month
print (name2+"'s date of birth:",date2) # print date
print(name2,"was born on",str(date2)+"/"+str(month2)+"/"+str(year2))
# print name with correct format


if (year2>year1): # 1st input older 
    print (name1,"is older than",name2)
elif (year2<year1): # 2nd input older
    print (name1,"is younger than",name2)
else: # years are equal
    if (month2>month1):
        print (name1,"is older than",name2)
    elif (month2<month1):
        print (name1,"is younger than",name2)
    else: #years & month are equal
        if (date1>date2):
            print (name2,"is older than",name1)
        elif (date1<date2):
            print (name2,"is younger than",name1)
        else: # years, month, & date equal
            print (name1,"and",name2,"are the exact same age")


