# import numpy as np
import pandas as pd
import csv

class HandleData:

    database = pd.read_csv('generated_data.csv')

    def getDatabse(self):
        return self.database


    def addNewSale(self, row):
        with open('generated_data.csv', mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def printDatabase(self):
        print(self.database)

    def deleteSales(self, delIndex):
        data_to_keep = []
        with open('generated_data.csv', mode='r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index != delIndex:
                    data_to_keep.append(row)
        print(data_to_keep)
        # Write the filtered data back to the CSV file
        with open('generated_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_to_keep)

    def get_mode(self, data):
        max_freq = 0
        modes = []
        count_dict = {}

        for num in data:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

            if count_dict[num] > max_freq:
                max_freq = count_dict[num]

        for num, freq in count_dict.items():
            if freq == max_freq:
                modes.append(num)

        return modes

    def get_median(self, data):
        sorted_data = sorted(data)
        length = len(sorted_data)
        middle = length // 2

        if length % 2 == 0:
            # If the length of the data is even, average the two middle values
            median = (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            # If the length of the data is odd, take the middle value
            median = sorted_data[middle]

        return median
    
    def get_mad(self, data, avg):
        sum_ = 0
        for sale in data:
            sum_ += abs(sale - avg)
        
        return sum_ / len(data)

    def get_sigma(self, data, avg):
        sum_ = 0
        for sale in data:
            point = abs(sale - avg)
            sum_ += (point**2)
        variance = sum_ / len(data)
        return variance**0.5
    
    def sales_METRICSTICS(self):
        total = 0
        count = 0
        column_index = 3
        sales = []
        with open('generated_data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                cell = row[column_index][1:]
                sales.append(int(cell))
                total += float(cell)
                count += 1
        # print(self.database)
        min_ = min(sales)
        max_ = max(sales)
        mode = self.get_mode(sales)
        median = self.get_median(sales)
        avg = sum(sales) / len(sales)
        mad = self.get_mad(sales, avg)
        sigma = self.get_sigma(sales, avg)
        return [min_, max_ , mode, median, avg, mad, sigma]