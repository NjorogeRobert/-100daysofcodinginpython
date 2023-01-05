'''The program calculates the years, months , weeks and days a person has left.
taking weeks to be 52 per year,days 365 per year, months 12 per year
'''
#Input age
age = input("What is your current age? ")

#change age to int from str
age_int = int(age)

years_left = (90 - age_int)

weeks_left = (years_left * 52)
months_left = (years_left * 12)
days_left = (years_left * 365)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")
