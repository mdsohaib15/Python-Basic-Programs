import calendar

yy = int(input("enter year: "))
mm = int(input("enter month: "))
print(calendar.month(yy,mm))

# print full calendar of 2024:

'''
for i in range(2024,2025):
          for j in range(1,13):
                    print(calendar.month(i,j))
'''

