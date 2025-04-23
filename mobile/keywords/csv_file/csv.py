import os, sys, csv
mobile_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(mobile_path)

class CSV:
    @staticmethod
    def get_file_path(file_name):
        return os.path.join(mobile_path, "resources", "testdata", file_name)
    
    @staticmethod
    def read_csv_data(file_name):
        data_file = CSV.get_file_path(file_name)
        with open(data_file, mode='r', newline='', encoding='utf-8') as file:
            data = csv.reader(file)
            next(data)
            return list(data)
    
    @staticmethod
    def write_csv_file(file_name, data):
        data_file = CSV.get_file_path(file_name)
        with open(data_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)