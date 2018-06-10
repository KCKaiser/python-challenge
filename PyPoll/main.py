import os, csv

pypollcsvpath = os.path.join('raw_data','election_data_1.csv')

identification=[]
county = []
names = []
with open(pypollcsvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    for row in csvreader:
        identification_start = row[0]
        county_start = row[1]
        names_start = row[2]

        identification.append(row[0])
        county.append(row[1])
        names.append(row[2])
    
    identification = identification[1:]
    county = county[1:]
    names = names[1:]

    num_votes = len(identification)
    print(num_votes)
    names_set = set(names)
    names_ls=list(names_set)
    names_sort= (sorted(names_ls))
    print(names_sort[0])

    
    
