line = "To be or not to be, that is the question"
print(line)

start_index = line.index(input("Choose a start point "))

end_index = line.index(input("Choose an end point "), start_index + 1)


middle = line[start_index + 1:end_index]


print(middle)
