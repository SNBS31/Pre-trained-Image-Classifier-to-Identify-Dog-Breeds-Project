state = 'CA'
purchase_amount = 20.00

if state == 'CA':
    tax_amount = 0.075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state,total_cost)
    
elif state == 'MN':
    tax_amount = 0.095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state,total_cost)   
    
elif state == 'NY':
    tax_amount = 0.089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state,total_cost)   
    
print(result)      