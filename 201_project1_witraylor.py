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

#4: Find the state with the highest sales average
def find_highest_avg_state(avg_dict):
    if avg_dict == {}:
        return None

    highest_state = max(avg_dict, key = avg_dict.get)
    highest_value = avg_dict[highest_state]

    return (highest_state, highest_value)

#5: Find the category with the highest total sales
def find_highest_cat(dict_list):
    category_totals = {}

    for sales_record in dict_list:
        category = sales_record['Category']
        sales = float(sales_record['Sales'])
        category_totals[category] = category_totals.get(category, 0) + sales

    if category_totals == {}:
        return None

    top_category = max(category_totals, key = category_totals.get)
    top_sales = round(category_totals[top_category], 2)

    return (top_category, top_sales)

#6: Write results into a txt file
def write_results(fname, avg_dict, top_state, top_category):
    with open(fname, 'w') as f:
        f.write("Average Sales by State\n")
        for state, avg in avg_dict.items():
            f.write(f"{state}: ${avg}\n")

        f.write("\nState with Highest Average Sales\n")
        f.write(f"{top_state[0]}: ${top_state[1]}\n")

        f.write("\nCategory with Highest Total Sales\n")
        f.write(f"{top_category[0]}: ${top_category[1]}\n")



#Test Cases
class Test(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {'State': 'Kentucky', 'Category': 'Furniture', 'Sales': '261.96'},
            {'State': 'Kentucky', 'Category': 'Furniture', 'Sales': '731.94'},
            {'State': 'California', 'Category': 'Office Supplies', 'Sales': '14.62'},
        ]

        self.sales_dicts = [
            {'Kentucky': ['Furniture', 261.96]},
            {'Kentucky': ['Furniture', 731.94]},
            {'California': ['Office Supplies', 14.62]},
        ]

        self.avg_dict = {
            'Kentucky': 496.95,
            'California': 14.62,
        }
    
    def test_calculate_avgs(self):
        result = calculate_avgs(self.sales_dicts)

        expected = {
            'Kentucky': round((261.96 + 731.94) / 2, 2),
            'California': 14.62,
        }

        result = calculate_avgs(self.sales_dicts)
        self.assertEqual(result, expected)

    def test_find_highest_avg(self):
        result = find_highest_avg_state(self.avg_dict)
        expected = ('Kentucky', 496.95)
        self.assertEqual(result, expected)

    def test_highest_cat(self):
        result = find_highest_cat(self.test_data)
        expected = ('Furniture', 993.9)
        self.assertEqual(result, expected)

    def test_empty_data(self):
        highest_avg_result = find_highest_avg_state({})
        highest_cat_result = find_highest_cat([])
        self.assertIsNone(highest_cat_result)
        self.assertIsNone(highest_avg_result)

    
def main():
    unittest.main(verbosity=2)
    dict_list = read_csv('SampleSuperstore.csv')
    sales_dicts = create_sales_dict(dict_list)
    avg_dict = calculate_avgs(sales_dicts)
    top_state = find_highest_avg_state(avg_dict)
    top_category = find_highest_cat(dict_list)

    write_results("sales_results.txt", avg_dict, top_state, top_category)

if __name__ == '__main__':
    main()