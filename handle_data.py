# import numpy as np
import pandas as pd
import csv

class HandleData:

    database = pd.read_csv('sales_data.csv')

    def getDatabse(self):
        return self.database


    def addNewSale(self, row):
        with open('sales_data.csv', mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def printDatabase(self):
        print(self.database)

    def deleteSales(self, delIndex):
        data_to_keep = []
        with open('sales_data.csv', mode='r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index != delIndex:
                    data_to_keep.append(row)
        print(data_to_keep)
        # Write the filtered data back to the CSV file
        with open('sales_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_to_keep)