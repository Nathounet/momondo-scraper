import csv
from operator import attrgetter
from datetime import datetime

class CsvWriter():
    def __init__(self, config_parameters, results_dep, results_ret):
        search_id = config_parameters.dep_date_min.strftime('%d-%m') + '_' + config_parameters.ret_date_max.strftime('%d-%m-%Y') + '_' + config_parameters.departure + '_' + config_parameters.arrival
        self.history_csv = './other_files/' + search_id
        # Write CSVs
        self.writeCSV(results_dep, 'Departures')
        self.writeCSV(results_ret, 'Returns')
        print 'Data stored in csv '+self.history_csv+'_***.csv'


    def writeCSV(self, results, way):
        history_csv_file = open(self.history_csv + '_'+way+'.csv', 'wt')
        history_csv_file_writer = csv.writer(history_csv_file, delimiter=';', lineterminator='\n')

        # Write Headers
        row = ['Date of scraping', datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        history_csv_file_writer.writerow(row)
        row = [ 'Flight type', 'Date of departure', 'Date of return','Price', 'Duration']
        history_csv_file_writer.writerow(row)
        for list_flight in results:
            # Cheapest flight of all

            ch_price_min = min(list_flight, key=attrgetter('cheapest_price'))
            row = [ 'Cheapest', ch_price_min.date_departure.strftime('%d-%m-%Y'), ch_price_min.date_return.strftime('%d-%m-%Y'), ch_price_min.cheapest_price, ch_price_min.cheapest_duration.toFloat() ]
            history_csv_file_writer.writerow(row)
            # Quickest of the cheapest flights
            ch_duration_min = min(list_flight, key=attrgetter('cheapest_duration.totalMinutes'))
            row = [ 'Quickest', ch_duration_min.date_departure.strftime('%d-%m-%Y'), ch_duration_min.date_return.strftime('%d-%m-%Y'), ch_duration_min.cheapest_price, ch_duration_min.cheapest_duration.toFloat() ]
            history_csv_file_writer.writerow(row)
            # Cheapest selected 'Best Deal' by Momondo
            bd_price_min = min(list_flight, key=attrgetter('bestdeal_price'))
            row = [ 'BestDeal', bd_price_min.date_departure.strftime('%d-%m-%Y'), bd_price_min.date_return.strftime('%d-%m-%Y'), bd_price_min.bestdeal_price, bd_price_min.bestdeal_duration.toFloat() ]
            history_csv_file_writer.writerow(row)
            history_csv_file_writer.writerow([''])
        history_csv_file.close()
