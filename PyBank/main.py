import glob, os, csv

# LOOPS THROUGH ALL THE .CSV FILES IN raw_data FOLDER
for filename in glob.glob('./raw_data/*.csv'):
    date = []
    rev = []
    with open(filename, newline = "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        for row in csvreader:
            # Creating list of Dates
            date.append(row[0])
            # Creating list of Revenue
            rev.append(row[1])
        # Getting rid of headers
        date = date[1:]
        rev = rev[1:]      

    # Convert Revnue into integers
    rev_num = [int(num) for num in rev]

    # Create a new list of Revenue Differences
    rev_diff = []
    for x in rev_num[:-1]:
        index1 = rev_num.index(x)
        index2 = rev_num.index(x)+1
        diff = (rev_num[index2] - rev_num[index1])
        rev_diff.append(diff)

    # Greatest Revenue Change (Max)
    diff_max = max(rev_diff)
    diffmax_index = rev_diff.index(diff_max)+1
    # Date of Greatest Revenue Change
    date_diff_max = date[diffmax_index] 

    # Least Revenue Change (Min)
    diff_min = min(rev_diff)
    diffmin_index = rev_diff.index(diff_min)+1
    # Date of Least Revenue Change
    date_diff_min = date[diffmin_index]

    # Total Months
    num_months = len(date)

    # Total Revenue
    rev_sum = sum(rev_num)

    # Average Revenue Change
    rev_diff_avg = sum(rev_diff)/float(len(rev_diff))

    # Create text file
    with open("." + filename[10:-4] + '.txt', 'w') as f:
        f.write("```\n")
        f.write("Financial Analysis (" + filename[11:-4] + ")\n")
        f.write("----------------------------\n")
        f.write("Total Months: " + str(num_months)+"\n")
        f.write("Total Revenue: $" + str(rev_sum)+"\n")
        f.write('Average Revenue Change: ' + "$" + "{:.2f}".format(rev_diff_avg) + "\n")
        f.write(f'Greatest Increase in Revenue: {date_diff_max} (${diff_max})\n')
        f.write(f'Greatest Decrease in Revenue: {date_diff_min} (${diff_min})\n')
        f.write("```")

    # Print
    print("```")
    print("Financial Analysis (" + filename[11:-4] + ")\n")
    print("----------------------------")
    print("Total Months: " + str(num_months))
    print("Total Revenue: $" + str(rev_sum))
    print('Average Revenue Change: ' + "$" + "{:.2f}".format(rev_diff_avg))
    print(f'Greatest Increase in Revenue: {date_diff_max} (${diff_max})')
    print(f'Greatest Decrease in Revenue: {date_diff_min} (${diff_min})')
    print("```")