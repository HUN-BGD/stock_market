import os


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

    def _download_stock_data(self, stock, start_year, end_year):
        dst_folder = self._get_stock_folder(stock)
        print(dst_folder)
        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder)
        for year in range(start_year, end_year+1):
            file_name = stock + '_' + str(year) + '.csv'
            print(os.path.join(dst_folder, file_name))

if __name__ == "__main__":
    nasdaq = StockMarket()
    nasdaq._download_stock_data('ATVI', 2015, 2018)
