import math
import csv

with open('data.csv', newline = '') as f:
  reader = csv.reader(f)
  file_data = list(reader)

data = file_data[0]

square_list = []

sum = 0

def find_mean(data):
  n = len(data)
  total =  0
  for i in data:
    total += int(i)
  mean = total/n
  return mean

for num in data:
  number = int(num) - find_mean(data)
  number = number**2
  square_list.append(number)

for i in square_list:
  sum = sum + i

result = sum/(len(data)-1)

standardDeviation = math.sqrt(result)

print()
print('Standard Deviation =', standardDeviation)
print()