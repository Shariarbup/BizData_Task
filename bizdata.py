# Todays date manipulation
todays_date=input("Enter todays date in this format(d/m/year): ")
todays_date_str = todays_date.split("/")
todays_date_int = [int(x) for x in todays_date_str]
to_day = todays_date_int[0]
to_mon = todays_date_int[1]
to_year = todays_date_int[2]

# user birthdate manipulation
user_date_of_birth=input("Enter your birth date in this format(d/m/y): ")
user_date_str = user_date_of_birth.split("/")
user_date_int = [int(x) for x in user_date_str]
print(user_date_int)
user_bday = user_date_int[0]
user_bmon = user_date_int[1]
user_byear = user_date_int[2]
print(user_bday)
print(user_bmon)
print(user_byear)


#For avoiding negative value in day and month
if(to_day < user_bday):
    to_mon = to_mon-1 
    to_day = to_day+30

if(to_mon < user_bmon):
    to_year = to_year-1
    to_mon = to_mon+12
print(to_year)


your_day = to_day-user_bday
your_mon = to_mon-user_bmon
your_year = to_year-user_byear
print("Your age is :",your_year," year",your_mon," month", your_day," day")



