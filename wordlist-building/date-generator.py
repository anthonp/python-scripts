# Generate all different dates from 1899-2030
# By Anthony P. Created 11/05/21

file = open("dates.txt", "w")
for date in range(1899, 2031):
        file.write(str(date))
        file.write('\n')
file.close()
