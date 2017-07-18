import csv
from operator import attrgetter
from datetime import datetime

class CsvWriter():
    def __init__(self, config_parameters, results_dep, results_ret):
        search_id = config_parameters.dep_date_min.strftime('%d-%m') + '_' + config_parameters.ret_date_max.strftime('%d-%m-%Y') + '_' + config_parameters.departure + '_' + config_parameters.arrival
        self.history_csv = './other_files/' + search_id
        # Write CSVs
        self.writeCSV(results_dep, results_ret)
        print 'Data stored in csv '+self.history_csv+'_***.csv'


    def writeCSV(self, results_dep, results_ret):
        ### Write Departures
        history_csv_file = open(self.history_csv + '_dep.csv', 'wt')
        history_csv_file_writer = csv.writer(history_csv_file, delimiter=';', lineterminator='\n')
        # Write Headers
        row = [ 'Date of scraping', 'Date of departure',
                'Cheapest.price', 'Cheapest.duration',
                'Quicker.price', 'Quicker.duration',
                'BestDeal.price', 'BestDeal.duration'
              ]
        history_csv_file_writer.writerow(row)
        for list_return_flight in results_dep:
            ch_price_min = min(list_return_flight, key=attrgetter('cheapest_price'))
            ch_duration_min = min(list_return_flight, key=attrgetter('cheapest_duration.totalMinutes'))
            bd_price_min = min(list_return_flight, key=attrgetter('bestdeal_price'))
            #print "{", ch_price_min.departure_date, "} ", "[Cheapest] price", ch_price_min.cheapest_price, "duration", ch_duration_min.cheapest_duration, "[BestDeal] price", bd_price_min.bestdeal_price
            row = [ datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ch_price_min.departure_date.strftime('%Y-%m-%d'),
                    ch_price_min.cheapest_price, ch_price_min.cheapest_duration.toFloat(),
                    ch_duration_min.cheapest_price, ch_duration_min.cheapest_duration.toFloat(),
                    bd_price_min.bestdeal_price, bd_price_min.bestdeal_duration.toFloat()
                  ]
            history_csv_file_writer.writerow(row)
        history_csv_file.close()

        ### Write Returns
        history_csv_file = open(self.history_csv + '_ret.csv', 'wt')
        history_csv_file_writer = csv.writer(history_csv_file, delimiter=';', lineterminator='\n')
        # Write Headers
        row = [ 'Date of scraping', 'Date of return',
                'Cheapest.price', 'Cheapest.duration',
                'Quicker.price', 'Quicker.duration',
                'BestDeal.price', 'BestDeal.duration'
              ]
        history_csv_file_writer.writerow(row)
        for list_departure_flight in results_ret:
            ch_price_min = min(list_departure_flight, key=attrgetter('cheapest_price'))
            ch_duration_min = min(list_departure_flight, key=attrgetter('cheapest_duration.totalMinutes'))
            bd_price_min = min(list_departure_flight, key=attrgetter('bestdeal_price'))
            #print "{", ch_price_min.departure_date, "} ", "[Cheapest] price", ch_price_min.cheapest_price, "duration", ch_duration_min.cheapest_duration, "[BestDeal] price", bd_price_min.bestdeal_price
            row = [ datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ch_price_min.return_date.strftime('%Y-%m-%d'),
                    ch_price_min.cheapest_price, ch_price_min.cheapest_duration.toFloat(),
                    ch_duration_min.cheapest_price, ch_duration_min.cheapest_duration.toFloat(),
                    bd_price_min.bestdeal_price, bd_price_min.bestdeal_duration.toFloat()
                  ]
            history_csv_file_writer.writerow(row)
        history_csv_file.close()
