# print specified month
import calendar
yy = 2006
mm = 6
print(calendar.month(yy,mm))

# print year,month of specified range
import calendar
for i in range(2006,2025):
    for j in range(1,12):
        print(calendar.month(i,j))