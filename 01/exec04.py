deposit = 10000
year = 0
interests = 0.0325
# interests = 0.10

money = deposit
total_income = 2 * deposit

while money < total_income:
    year += 1
    money = money*(1+interests)
    # print money

print "Need %d years." % year
