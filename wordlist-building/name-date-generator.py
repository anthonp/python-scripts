# Generate usernames with dates from 1899-2030 with topic
# By Anthony P. Created 11/05/21

example = "anna"
topic = "soccer"
file = open("name-dates.txt", "w")
for date in range(1899, 2031):
        file.write(example + str(date) + topic)
        file.write('\n')
file.close()
