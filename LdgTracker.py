import csv
from curses.ascii import isdigit
from tkinter import N

def write(score):
    if score.isdigit() is False:
        print("Inputted score is not a number, try again")
        return
    row = [score]
    with open('./LDG.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def stats():
    with open('./LDG.csv', 'r') as f:
        reader = csv.reader(f)
        avg = average(reader)
        recent_avg = recent_average(reader)
        max = max(reader)
        print(f"Your overall average is {avg}")
        print(f"Your recent average over 20 runs is {recent_avg}")
        print(f"Your max score is {max}")
        
def average(f):
    avg = 0 
    sum = 0
    row_count = 0
    for row in f:
        n = float(row[0])
        sum += n
        row_count += 1
    if row_count == 0:
        return 0
    avg = sum / row_count
    return avg

def recent_average(f):
    avg = 0
    sum = 0
    row_count = 0
    for row in f:
        row_count += 1
        if row_count == 20:
            break
    print(row_count)
    first_index = row_count * -1
    rows = []
    for row in f:
        rows.append(row)
    for row in rows[first_index:]:
        n = row[0]
        sum += n
    
    avg = sum / row_count
    return avg

def max(f):
    max = 0
    for row in f:
        n = float(row)
        if n > max:
            max = row
    return max

stats()
print("Press Ctrl C to break")
while True:
    print("Enter your score")
    score = input()
    write(score)
write("19")
