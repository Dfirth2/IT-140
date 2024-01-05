# get name as a string
name = input("What is your name? \n")
# get age as an int
age = int(input("How old are you? \n"))
# calculate birth year
from datetime import date
current_year = date.today().year
birth_year = current_year - age
# print greeting
print(f"Hello {name}! You were born in {birth_year}.")