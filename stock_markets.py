import os
import datetime
import pandas
import pandas_datareader
import numpy


class StockMarket():
    def __init__(self, data_root='data'):
        self.name = 'NASDAQ'
        self.data_root = data_root

    def list_folder(self):
        os.listdir()
        print(self.data_root)
        print(os.listdir(self.data_root))

    def _get_stock_folder(self, stock):
        return os.path.join(self.data_root, self.name, stock)

    def _download_data_from_yahoo(self, stock, year):
        start = datetime.datetime(year, 1, 1)
        end = datetime.datetime(year, 12, 31)

        stock_data = pandas_datareader.DataReader(stock, 'yahoo', start, end)
        return stock_data

    def _download_stock_data(self, stock, start_year, end_year):
        dst_folder = self._get_stock_folder(stock)

        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder)

        for year in range(start_year, end_year+1):
            file_name = stock + '_' + str(year) + '.csv'
            file_path = os.path.join(dst_folder, file_name)

            if not os.path.isfile(file_path):
                stock_data = self._download_data_from_yahoo(stock, year)
                stock_data.to_csv(file_path)



if __name__ == "__main__":
    nasdaq = StockMarket()
    nasdaq._download_stock_data('ATVI', 2000, 2018)
    nasdaq._download_stock_data('GE', 2015, 2018)

    stock_data = pandas.read_csv(r'C:\Users\Dani\Desktop\Pycharm\stock_market\data\NASDAQ\ATVI\ATVI_2000.csv')


    # Random trader
    my_money = 100000.0
    my_stock = 0
    activity = 0.3

    for i in range(len(stock_data.index)):
        if numpy.random.random() < activity:
            open_price = stock_data.iloc[i]["Open"]
            if my_money > 0:
                my_stock = my_money / open_price
                my_money = 0
            else:
                my_money = open_price * my_stock
                my_stock = 0
                print("Now I have:", int(numpy.round(my_money)))
