### PyBank analysis 

import os
import csv

budget_csvpath = os.path.join('Resources', 'budget_data.csv')

with open(budget_csvpath, newline='') as budget_csvfile:

	budget_csvreader = csv.reader(budget_csvfile, delimiter=',')

	budget_list = list(budget_csvreader)
	head_budget_list = budget_list[0]
	data_budget_list = budget_list[1:]

	total_months = len(data_budget_list)

	net_total = 0
	change = 0
	prev_row = ['','']

#	avg_change = round(int(data_budget_list[-1][1])-int(data_budget_list[0][1]),2)
	
	row_max = ['','0']
	row_min = ['','0']


	for row in data_budget_list:
		net_total += int(row[1])

		if int(row[1]) > int(row_max[1]):
			row_max = row
		elif int(row[1]) < int(row_min[1]):
			row_min = row

		if row != data_budget_list[0]:
			change += int(row[1]) - int(prev_row[1])

		prev_row = row

	#row_max is Increase
	#row_min is Decrease

	avg_change = round(change/total_months,2)

# ````````````````Print Statements``````````````````````

	print('```text')
	print('Financial Analysis')
	print('------------------')
	print(f'Total Months: {total_months}')
	print(f'Total: ${net_total}')
	print(f'Average Change: ${avg_change}')
	print(f'Greatest Increase in Profits: {row_max[0]} (${row_max[1]})')
	print(f'Greatest Decrease in Profits: {row_min[0]} (${row_min[1]})')
	print('````')

output_path = os.path.join('Resources','summary.txt')

summary = open(output_path, 'w')
summary.write('```text\n')
summary.write('Financial Analysis\n')
summary.write('------------------\n')
summary.write(f'Total Months: {total_months}\n')
summary.write(f'Total: ${net_total}\n')
summary.write(f'Average Change: ${avg_change}\n')
summary.write(f'Greatest Increase in Profits: {row_max[0]} (${row_max[1]})\n')
summary.write(f'Greatest Decrease in Profits: {row_min[0]} (${row_min[1]})\n')
summary.write('````')
summary.close()

