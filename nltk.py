import nltk
import csv


employees = [
    'name1-surname1-place1',
    'name2-surname2-place2',
    'name3-surname3-place3',
    'name4-surname4-place4',
 ]
with open('out.csv', 'w') as out:
    writer = csv.writer(out)
    for e in employees:
        writer.writerow(e.split("-"))
# with open('egg.csv', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f,delimiter=' ', quoting=csv.QUOTE_ALL)
#     for row in reader:
#         print(row[1])
