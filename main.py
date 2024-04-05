import pandas as pd
from collections import Counter
import statistics as stats
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('powerball.csv')

# Split the 'Winning Numbers' column into a list of numbers
df['Winning Numbers'] = df['Winning Numbers'].apply(lambda x: list(map(int, x.split())))

# Flatten the list of lists into a single list
all_numbers = [num for sublist in df['Winning Numbers'].tolist() for num in sublist]

# Create a Counter object to count the occurrence of each number
counter = Counter(all_numbers)

# Print the count of each number
for num, count in counter.items():
    print(f'Number {num} has occurred {count} times')

# Print the most common number
most_common_num, most_common_count = counter.most_common(1)[0]
print(f'The most common number is {most_common_num} with {most_common_count} occurrences')

# Print the least common number
least_common_num, least_common_count = counter.most_common()[-1]
print(f'The least common number is {least_common_num} with {least_common_count} occurrences')

# Print the average of all numbers
average = sum(all_numbers) / len(all_numbers)
print(f'The average of all numbers is {average}')

# Print the median of all numbers
median = stats.median(all_numbers)
print(f'The median of all numbers is {median}')

# Print the standard deviation of all numbers
std_dev = stats.stdev(all_numbers)
print(f'The standard deviation of all numbers is {std_dev}')

# Print the mode of all numbers
mode = stats.mode(all_numbers)
print(f'The mode of all numbers is {mode}')

# Print the variance of all numbers
variance = stats.variance(all_numbers)
print(f'The variance of all numbers is {variance}')

# Print the minimum and maximum number
min_num = min(all_numbers)
max_num = max(all_numbers)
print(f'The minimum number is {min_num} and the maximum number is {max_num}')

# Get the top 6 most common numbers
most_common_numbers = [num for num, _ in counter.most_common(6)]
print(f'The top 6 most common numbers are: {most_common_numbers}')

# Get the top 6 least common numbers
least_common_numbers = [num for num, _ in counter.most_common()[:-7:-1]]
print(f'The top 6 least common numbers are: {least_common_numbers}')

# Plot the frequency distribution of numbers
plt.hist(all_numbers, bins=range(min_num, max_num+1), alpha=0.7, edgecolor='black')
plt.title('Frequency Distribution of Numbers')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.show()

# Plot the cumulative frequency of numbers
plt.hist(all_numbers, bins=range(min_num, max_num+1), cumulative=True, alpha=0.7, edgecolor='black')
plt.title('Cumulative Frequency of Numbers')
plt.xlabel('Number')
plt.ylabel('Cumulative Frequency')
plt.show()
