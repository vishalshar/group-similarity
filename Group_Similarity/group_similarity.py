import csv
import pandas as pd
import numpy as np
from scipy import spatial
import operator
import math



data = pd.read_csv('./random_data.csv', delimiter=',')

# print type(data)
# print data.shape
#
# print data.columns.values
# print len(data.columns.values)


# Given Player
# name = r
# year = 2000 - 2005
# find other similar player with similar 4 and 6

r_data = data[(data['name'] == 'r') & (data['year'] >= 2000) & (data['year'] <= 2005)]
r_data = r_data[['number of 4','number of 6']]
r_data_sum = np.sum(r_data, axis = 0)

# print r_data.shape
results = {}

# Get all players name
player_names = data.name.unique()
# print len(player_names)
# print player_names[0]

# Remove player 'r'
player_names = np.delete(player_names, (player_names.tolist()).index('r'))
# print player_names

def cosine_similarity(x, y):
    return (1 - spatial.distance.cosine(x, y))



################
## Similarity based on sum of all vectors and finding similarity of two points
################

for name in player_names:
    player_data = data[(data['name'] == name) & (data['year'] >= 2000) & (data['year'] <= 2005)]
    player_data = player_data[['number of 4','number of 6']]
    sum_data = np.sum(player_data, axis = 0)
    sim_score = cosine_similarity(sum_data.values, r_data_sum.values)
    results[name] = sim_score
    print name, sim_score


print "\nresult"
sorted_x = sorted(results.items(), key=operator.itemgetter(1),reverse=True)
print sorted_x[0]



################
## Similarity based on closest vector in two groups
################
closest_player_name = ''
closest_player_score = 10000

def get_distance(x1,y1, x2,y2):
    return math.hypot(x2 - x1, y2 - y1)


def get_closest_distance(player_data, r_data):
    shortest_distance = 10000
    for index_r, row_r in r_data.iterrows():
        for index_p, row_p in player_data.iterrows():
            dist = get_distance(row_r['number of 4'], row_r['number of 6'], row_p['number of 4'], row_p['number of 6'])
            if shortest_distance > dist:
                shortest_distance = dist
    return shortest_distance


for name in player_names:
    player_data = data[(data['name'] == name) & (data['year'] >= 2000) & (data['year'] <= 2005)]
    player_data = player_data[['number of 4','number of 6']]
    dist_score = get_closest_distance(player_data, r_data)

    print dist_score, name
    if closest_player_score > dist_score:
        closest_player_score = dist_score
        closest_player_name = name

    # print closest_player_name, closest_player_score

print closest_player_name, closest_player_score


################
## Similarity based on similar cluster (top 5 similar score)
################
k = 5

def get_close_distance_k(player_data, r_data):
    shortest_distance = []
    for index_r, row_r in r_data.iterrows():
        for index_p, row_p in player_data.iterrows():
            dist = get_distance(row_r['number of 4'], row_r['number of 6'], row_p['number of 4'], row_p['number of 6'])
            shortest_distance.append(dist)
    shortest_distance.sort()
    sim = sum(shortest_distance[0:5])
    return sim


for name in player_names:
    player_data = data[(data['name'] == name) & (data['year'] >= 2000) & (data['year'] <= 2005)]
    player_data = player_data[['number of 4','number of 6']]
    dist_score = get_close_distance_k(player_data, r_data)

    print dist_score, name
    if closest_player_score > dist_score:
        closest_player_score = dist_score
        closest_player_name = name

    print closest_player_name, closest_player_score

print closest_player_name, closest_player_score




