

def weekday(day):
  
  if (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday"):
    print(day, " is working day.")
  elif (day == "saturday" or day == "sunday"):
    print(day, " is holiday.")
  else:
    print(day, " it is not day ")


day = str(input("Enter day: "))
weekday(day)

