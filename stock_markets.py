import os


class StockMarket():
    def __init__(self, data_root='.'):
        self.name = 'NASDAQ'
        self.data_root = data_root

    def list_folder(self):
        os.listdir()
        print(self.data_root)
        print(os.listdir(self.data_root))

    def get_stock_folder(self, stock):
        return self.data_root + self.name + '/' + stock + '/'


if __name__ == "__main__":
    nasdaq = StockMarket('c://')
    print(nasdaq.name)

    "data_root/name/stickername"

    nasdaq.list_folder()
    nasdaq.get_stock_folder('ATVI')
    vmi = nasdaq.get_stock_folder('ATVI')

    print(vmi)