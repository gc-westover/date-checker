date1 = [ 3, 4, 2021 ]
date2 = [ 3, 3, 2021 ]

def dateCode(dateArray):
  return 100*dateArray[2] + 10*dateArray[0] + dateArray[1]

def compareDates(d1,d2):
  if dateCode(d1) < dateCode(d2):
    print("Date 1 earlier")
  elif dateCode(d1) == dateCode(d2):
    print("same date")
  else:
    print("Date 1 later")

compareDates(date1,date2)