#Name: Willow Traylor
#Student ID: 67975434
#Email: wtraylor@umich.edu
#Collaborators: 

import csv
import os

#1: read the csv file
def read_csv(filename):
    data = []
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, filename)

    with open(file_path, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    return data


#2: create list of dictionaries with states and their sales
def create_sales_dict(dict_list):
    sales_dict = {}
    for dict in dict_list:
        state = dict['State'] 
        if state not in sales_dict.keys():
            sales_list = []
            sales_list.append(dict['Category'])
            sales = dict['Sales'].replace("'", "")
            sales_list.append(sales)
            sales_dict[state] = sales_list
    return sales_dict

#3: Calculate average sales in each state



dict_list = read_csv('SampleSuperstore.csv')
print(create_sales_dict(dict_list))