def is_leap(year):
    if (year%400==0) or (year%4==0 and year %100 !=0):
        return True
    else:
        return False
while True:
    year_input=input("Enter a 4 digit year:") 
    if len (year_input)==4 and year_input.isdigit():
        year=int(year_input)
        if is_leap(year):
            print(f"(year) is a leap year.")
        else:
            print(f"(year) is not a leap year.")

