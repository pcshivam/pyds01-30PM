input_year = int(input("Please enter the year : "))

if input_year %4 == 0:
  print (input_year," is a leap year" )

else:
  print (input_year," is not a leap year")

def check_even(i):
  if i%2 == 0:
    print("Even")

  else:
    print("odd")