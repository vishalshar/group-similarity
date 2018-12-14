# Random Data Generator for innings in cricket
##########################
## Data Fields
# name: [a,z]
# year: [1988, 2010]
# 4's: [0, 25]
# 6's: [0, 15]
# team: [1,5]

## Below three which needs synchronization
# win: {0, 1}
# loss: {0, 1}
# draw: {0, 1}
##########################
from random import *
import csv



# File to write final scores
target = open('./random_data.csv', 'wb')
csvwriter = csv.writer(target, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow(['Id','name', 'year', 'number of 4', 'number of 6', 'team', 'win', 'loss', 'draw'])



def getChars():
    char = []
    for one in range(97, 123):
        char.append(chr(one))
    return char

items = getChars()
teams = ['aa', 'bb', 'cc', 'dd', 'ee']
n = 10000

count = 0

for i in range(n):
    name = sample(items, 1)
    year = randint(1988, 2010)
    numberOf_4 = randint(0, 25)
    numberOf_6 = randint(0, 15)
    team = sample(teams, 1)

    # Win, Loss, Draw
    w_l_d = randint(0, 2)
    temp = [0] * 3
    temp[w_l_d] = 1

    count += 1

    #     name     year     4's        6's        win      loss    draw      team
    print name[0], year, numberOf_4, numberOf_6, temp[0], temp[1], temp[2], team[0]
    csvwriter.writerow([count, name[0], year, numberOf_4, numberOf_6, team[0], temp[0], temp[1], temp[2]])
