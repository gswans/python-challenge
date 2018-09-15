# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Model for formating currency
import locale

# csvpath = '../Resources/budget_data.csv'

csvpath = os.path.join('.','Resources', 'election_data.csv')


#print(csvpath)


# Method: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    
    next(csvreader)  
    # Candidate Options and Vote Counters
    candidate = []
    candidate_votes = {}
    total_votes = 0
    khancount = 0
    correycount = 0
    licount = 0
    tooleycount = 0
    
    for row in csvreader:


        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        if candidate_name == "Khan":
            khancount = khancount + 1
        elif candidate_name == "Correy":
            correycount = correycount + 1
        elif candidate_name == "Li":
            licount = licount + 1
        else:
            tooleycount = tooleycount + 1
        
        khanpercent = (khancount/total_votes)*100
        correypercent = (correycount/total_votes)*100
        lipercent = (licount/total_votes)*100
        tooleypercent = (tooleycount/total_votes)*100
        
    print("Election Results")
    print("_______________________________")
    print("Total Votes: " + str(total_votes))
    print("________________________________")
    print("Khan " + str(khanpercent)+"% "+ "("+str(khancount)+")")
    print("Correy: " + str(correypercent)+"% "+ "("+str(correycount)+")" )
    print("Li: " + str(lipercent)+"% "+ "("+str(licount)+")" )
    print("O'Tooley: " + str(tooleypercent)+"% "+ "("+str(tooleycount)+")" )
    print("________________________________")
    print("Winner: " + "Khan")

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        #if candidate_name not in candidate:

            # Add it to the list of candidates in the running
        #    candidate.append(candidate_name)

        # And begin tracking that candidate's voter count
        #candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        
       # candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
    #print(total_votes)
    #print(candidate)
    #print(len(candidate_votes))