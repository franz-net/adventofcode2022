# Read input
with open("Day1/input.txt", "r") as file:
   data = file.read()


# Brute Force Solution Part 1
max_cals = 0
current_sum = 0
for x in data.split('\n'):
    if x != '':
        current_sum+=int(x)
    else:
        if current_sum > max_cals:
            max_cals = current_sum
        current_sum = 0

print(max_cals)

# Re-optimization for part 2

current_sum = 0
sums_list = []

for x in data.split('\n'):
    if x != '':
        current_sum+=int(x)
    else:
        sums_list.append(current_sum)
        current_sum = 0

sums_list.sort(reverse=True)

print(sums_list[0] + sums_list[1] + sums_list[2])
