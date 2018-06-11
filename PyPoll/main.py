import os, csv, glob, collections

# LOOP THROUGH ALL THE .CSV FILES IN raw_data FOLDER
for filename in glob.glob('./raw_data/*.csv'):

    identification=[]
    names = []
    with open(filename, newline = "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        for row in csvreader:
            # Creating list of IDs
            identification.append(row[0])
            # Creating list of Candidates voted
            names.append(row[2])
        # Getting rid of headers
        identification = identification[1:]
        names = names[1:]
    
    # Number of votes
    num_votes = len(identification)

    # Converting names to set format to find unique candidates
    candidates_set = set(names)
    # Converting the set back to list format
    candidates_ls = list(candidates_set)
    # Sort list of candidates alphabetically
    candidate_list= (sorted(candidates_ls))

    # Sort the full list of candidates voted alphabetically
    full_names_sort= (sorted(names))

    # Go through full list of candidates names to count votes and calculate percentage
    count = {}
    percent = {}
    for x in candidate_list:
        counter = full_names_sort.count(x)
        count[x]= counter
        percent[x] = (count[x]/num_votes)

    # Determine which candidates received highest number of votes
    win = collections.Counter(count)
    winning = win.most_common(1)

    # Write text file
    with open('.' + filename[10:-4] + '.txt', 'w') as f:
        f.write('```\n')
        f.write('Election Results (' + filename[11:-4] + ')\n')
        f.write('-------------------------\n')
        f.write('Total Votes: ' + str(num_votes) + "\n")
        f.write('-------------------------\n')
        for x in candidate_list:
            f.write(f'{x}:  {percent[x]:.1%} ({count[x]}) \n')
        f.write('-------------------------\n')
        f.write('Winner: ' + winning[0][0] +'\n')
        f.write('-------------------------\n')
        f.write('```')

    # Print
    print('```')
    print('Election Results (' + filename[11:-4] + ")")
    print('-------------------------')
    print('Total Votes: ' + str(num_votes))
    print('-------------------------')
    for x in candidate_list:
        print(f'{x}:  {percent[x]:.1%} ({count[x]})')
    print('-------------------------')
    print('Winner: ' + winning[0][0])
    print('-------------------------')
    print('```')
