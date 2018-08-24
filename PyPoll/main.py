### PyPoll 

import os
import csv

election_csvpath = os.path.join('Resources','election_data.csv')

with open(election_csvpath,newline='') as election_csv:
    election_csvreader = csv.reader(election_csv, delimiter=',')

    election = list(election_csvreader)
    election_head = election[0]
    election_data = election[1:]

    total_votes = len(election_data)

    candidate_pool = {}

    for vote in election_data:
        if vote[2] not in candidate_pool:

            candidate_pool[vote[2]] = 1
        else:

            candidate_pool[vote[2]] += 1

    print(candidate_pool)

print('Election Results!')
print('----------------------')
print(f'Total Votes: {total_votes}')
print('----------------------')
for key in candidate_pool:
    print(f'{key}: {round((candidate_pool[key]/total_votes)*100,2)}% ({candidate_pool[key]})')
print('----------------------')
winner = max(candidate_pool, key=candidate_pool.get)
print(f'Winner is: {winner}')
