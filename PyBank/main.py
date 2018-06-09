import os, csv

pybankcsvpath = os.path.join('raw_data','budget_data_2.csv')

date=[]
rev = []
with open(pybankcsvpath, newline = "") as csvfile:
    print(csvfile)
    csvreader = csv.reader(csvfile, delimiter = ',')

    for row in csvreader:
        date_start = row[0]
        rev_start = row[1]
        date.append(row[0])
        rev.append(row[1])
    date = date[1:]
    rev = rev[1:]

    rev_num = [int(num) for num in rev]

    rev_max = max(rev_num)
    rev_min = min(rev_num)
    
    min_index =rev_num.index(rev_min)
    max_index =rev_num.index(rev_max)

    date_min = date[min_index]
    date_max = date[max_index]

    num_months = len(date)

    rev_sum = sum(rev_num)
    rev_avg = float(sum(rev_num))/len(rev_num)
    print(rev_avg)

    print("```")
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(num_months))
    print("Total Revenue: $" + str(rev_sum))
    print("Average Revenue Change: $" + str(rev_avg))
    print(f'Greatest Increase in Revenue: {date_max} (${rev_max})')
    print(f'Greatest Decrease in Revenue: {date_min} (${rev_min})')
    print("```")

    filename = 'budget_data_2.txt'
    with open(filename,'w') as f:
        f.write("```\n")
        f.write("Financial Analysis\n")
        f.write("----------------------------\n")
        f.write("Total Months: " + str(num_months)+"\n")
        f.write("Total Revenue: $" + str(rev_sum)+"\n")
        f.write("Average Revenue Change: $" + str(rev_avg)+"\n")
        f.write(f'Greatest Increase in Revenue: {date_max} (${rev_max})\n')
        f.write(f'Greatest Decrease in Revenue: {date_min} (${rev_min})\n')
        f.write("```")




        