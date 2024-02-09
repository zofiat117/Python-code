L = [5.9, 3.95, 5.82, 3.43, 5.52, 2.35, 4.78, 5.55, 10.88, 7.42, 5]

# Build up a list of unique values
unique_values = []
for value in L:
    if value not in unique_values:
        unique_values.append(value)

# Build up a list of frequencies
frequencies = []
for value in unique_values:
    frequency = L.count(value)
    frequencies.append(frequency)

# Find the mode
max_frequency = max(frequencies)
max_frequency_pos = frequencies.index(max_frequency)
mode = unique_values[max_frequency_pos]

print("Mode is", mode)

L = [41.37, 27.73, 40.75, 10.35, 32, 16.37, 19.13, 38.9, 76.28, 29.72, 30]

# Build up a list of unique values
unique_values = []
for value in L:
    if value not in unique_values:
        unique_values.append(value)

# Build up a list of frequencies
frequencies = []
for value in unique_values:
    frequency = L.count(value)
    frequencies.append(frequency)

# Find the mode
max_frequency = max(frequencies)
max_frequency_pos = frequencies.index(max_frequency)
mode = unique_values[max_frequency_pos]

print("Mode is", mode)
