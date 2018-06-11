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

    # Revenue Max
    rev_max = max(rev_num)
    max_index = rev_num.index(rev_max)
    # Date of Max Revanue
    date_max = date[max_index] 

    # Revnue Min
    rev_min = min(rev_num) 
    min_index = rev_num.index(rev_min)
    # Date of Min Revenue
    date_min = date[min_index]

    # Total Months
    num_months = len(date)

    # Total Revenue
    rev_sum = sum(rev_num)
    # Average Revenue
    rev_avg = rev_sum/len(rev_num)

    # Create text file
    with open("." + filename[10:-4] + '.txt', 'w') as f:
        f.write("```\n")
        f.write("Financial Analysis (" + filename[11:-4] + ")\n")
        f.write("----------------------------\n")
        f.write("Total Months: " + str(num_months)+"\n")
        f.write("Total Revenue: $" + str(rev_sum)+"\n")
        f.write('Average Revenue Change: ' + "$" + "{:.2f}".format(rev_avg) + "\n")
        f.write(f'Greatest Increase in Revenue: {date_max} (${rev_max})\n')
        f.write(f'Greatest Decrease in Revenue: {date_min} (${rev_min})\n')
        f.write("```")

    # Print
    print("```")
    print("Financial Analysis (" + filename[11:-4] + ")\n")
    print("----------------------------")
    print("Total Months: " + str(num_months))
    print("Total Revenue: $" + str(rev_sum))
    print('Average Revenue Change: ' + "$" + "{:.2f}".format(rev_avg))
    print(f'Greatest Increase in Revenue: {date_max} (${rev_max})')
    print(f'Greatest Decrease in Revenue: {date_min} (${rev_min})')
    print("```")

