def leap_year(year):
    leap = True
    if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 400 == 0) and (year % 100 == 0)):
      return leap
    else:
        leap=False
        return leap
year = int(input("Please, Enter the year: "))
print (leap_year(year))
'''
Test case 1
Input Format
1990
Output Format
False
----------------------------
Test case 2
Input Format
1992
Output Format
True
-----------------------------
Test case 3
Input Format
1993
Output Format
False
-----------------------------
Test case 4
Input Format
1996
Output Format
True
'''
