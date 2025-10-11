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
    avg_dict = {}
    for dict in sales_dicts:
        for k, v in dict.items():
            if k not in avg_dict:
                avg_dict[k] = v[1]
            else: 
                avg_dict[k] += v[1]
        for k, v in avg_dict.items():
            avg_dict[k] 
    return f"Here are the averages: {avg_dict}"


dict_list = read_csv('SampleSuperstore.csv')
sales_dict = create_sales_dict(dict_list)
print(sales_dict)



class Test(unittest.TestCase):
    def setUp(self):
        self.dict_list = read_csv('SampleSuperstore.csv')
        self.sales_dict = create_sales_dict(self.dict_list)[:5]
        self.avg_dict = calculate_avgs(self.sales_dict)

    def test_calculate_avgs(self):
        self.sales_dict.assertEqual(calculate_avgs, )
    
    def test_find_highest_avg(self):
        self.avg_dict.assertEqual(find_highest_avg, )

    def test_find_highest_cat(self):
        self.sales_dict.assertEqual(find_highest_cat, )




    


def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()