#leaf year
"""
year % 4 ==0 &
year % 100 != 0 /
year % 400 == 0

"""


def isleafyear(year):
  if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = 2012

if isleafyear(year):
  print('{} is a leaf year.'.format(year))
else:
  print('{} is not a leaf year.'.format(year))