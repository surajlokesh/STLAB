def check( day, month):
    if((month==4 or month==6 or month==9 or month==11) and day==31):
        return 1
    else:
        return 0
def isleap( year):
    if((year%4==0 and year%100!=0) or year%400==0):
        return 1
    else:
        return 0 
flag='n'        
while(flag=='n'):
    flag='y' 
    print("\nEnter the today's date in the form of dd mm yyyy\n")
    #scanf("%d%d%d",&day,&month,&year);
    day=int(input())
    month=int(input())
    year=int(input())
    tomm_day=day+1
    tomm_month=month
    tomm_year= year
    if(day<1 or day>31):
        print("Value of day, not in the range 1...31\n")
        flag='n'
    if(month<1 or month>12):
        print("Value of month, not in the range 1....12\n")
        flag='n'
    elif(check(day,month)):
        print("Value of day, not in the range day<=30")
        flag='n'
    if(year<1812 or year>2014):

        print("Value of year, not in the range 1812.......2014\n")
        flag='n'                
    if(month==2):
        if(isleap(year) and day>29):
            print("Invalid date input for leap year")
            flag='n'
        elif(not(isleap(year)) and day>28):
            print("Invalid date input for not a leap year")
            flag='n'    

if(month==10):
    if(day<31):
        tomm_day=day+1
    else:
        tomm_day=1
        tomm_month=month+1
if(month==11):
    if(day<30):
        tomm_day=day+1
    else:
        tomm_day=1
        tomm_month=month+1
if(month==12):
    if(day<31):
        tomm_day=day+1
    else:
        tomm_day=1
        tomm_month=1
        if(year==2014):
            print("The next day is out of boundary value of year\n")
            tomm_year=year+1
        else:
            tomm_year=year+1  
if(month==2):
    if(day<28):
        tomm_day=day+1
    elif(isleap(year) and day==28):
        tomm_day=day+1
    elif(day==28 or day==29):
        tomm_day=1
        tomm_month=3
print("Next day is ",tomm_day,tomm_month,tomm_year)