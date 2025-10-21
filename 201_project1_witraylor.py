#Name: Willow Traylor
#Student ID: 67975434
#Email: wtraylor@umich.edu
#Collaborators: 

import unittest
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
    out_list = []
    for dict in dict_list:
        state = dict['State'] 
        sales_dict = {}
        sales_list = []
        sales_list.append(dict['Category'])
        sales_list.append(float(dict['Sales']))
        sales_dict[state] = sales_list
        out_list.append(sales_dict)
    return out_list

#3: Calculate average sales in each state
def calculate_avgs(sales_dicts):
    totals = {}
    counts = {}
    avg_dict = {}

    for dict in sales_dicts:
        for state, sales in dict.items():
            sales_amount = sales[1]
            if state not in totals:
                totals[state] = sales_amount
                counts[state] = 1
            else: 
                totals[state] += sales_amount
                counts[state] += 1

        for state in totals:
            avg_dict[state] = round(totals[state] / counts[state], 2)
    print(f"Here are the averages: {avg_dict}")
    return avg_dict

def find_highest_avg_state(avg_dict):
    if avg_dict == {}:
        return None

    highest_state = max(avg_dict, key=avg_dict.get)
    highest_value = avg_dict[highest_state]

    return (highest_state, highest_value)


#dict_list = read_csv('SampleSuperstore.csv')
#sales_dict = create_sales_dict(dict_list)
#print(sales_dict)




class Test(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {'State': 'Kentucky', 'Category': 'Furniture', 'Sales': '261.96'},
            {'State': 'Kentucky', 'Category': 'Furniture', 'Sales': '731.94'},
            {'State': 'California', 'Category': 'Office Supplies', 'Sales': '14.62'},
        ]
        self.sales_dicts = [
            {'Kentucky': ['Furniture', 261.96]},
            {'Kentucky': ['Furniture', 731.94]},
            {'California': ['Office Supplies', 14.62]},
        ]
    
    def test_calculate_avgs(self):
        result = calculate_avgs(self.sales_dicts)

        expected = {
            'Kentucky': round((261.96 + 731.94) / 2, 2),
            'California': 14.62,
        }

        result = calculate_avgs(self.sales_dicts)
        self.assertEqual(result, expected)

    




    


def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()