def is_leap(year):
    leap = False
    
    # Write your logic here
    if year >= 1900 and year <= 10**5:
        """
        if year%4 == 0:
            leap = True
        elif year%100 == 0 and year%400 == 0:
            leap = True
        """
        if year % 4 == 0 and year % 100 != 0:
            leap = True
        elif year % 4 == 0 and year % 100 == 0:
            if year % 400 != 0:
                leap = False
            else:
                leap = True
        else:
            leap = False
                
    return leap

year = int(input("Type the year you want to check: ))
print(is_leap(year))
