mon_sales = '121'
tues_sales = '105'
wed_sales = '110'
thurs_sales = '98'
fri_sales = '95'

weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales) #Now converting our int result back

result_string = "The week's total sales is: " + weekly_sales

print(result_string)