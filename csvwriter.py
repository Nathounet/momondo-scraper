import csv
from operator import attrgetter

class CsvWriter():
    def __init__(self, config_parameters, results_dep, results_ret):
        self.search_id = config_parameters.dep_date_min.strftime('%d-%m') + '_' + config_parameters.ret_date_max.strftime('%d-%m-%Y') + '_' + config_parameters.departure + '_' + config_parameters.arrival

        history_csv = './other_files/' + self.search_id
        history_csv_file = open(history_csv + '_dep.csv', 'wt')
        history_csv_file_writer = csv.writer(history_csv_file, delimiter=',', lineterminator='\n')
        # Write Departures
        history_csv_file_writer.writerow(['Date of departure','Cheapest price','Cheapest duration 10','Cheapest duration 60','Quicker price','Quicker duration 10','Quicker duration 60','Best Deal price','Best Deal duration 10','Best Deal duration 60'])
        for everyReturnList in results_dep:
            ch_price_min = min(everyReturnList, key=attrgetter('cheapest_price'))
            ch_duration_min = min(everyReturnList, key=attrgetter('cheapest_duration.totalMinutes'))
            bd_price_min = min(everyReturnList, key=attrgetter('bestdeal_price'))
            #print "{", ch_price_min.departure_date, "} ", "[Cheapest] price", ch_price_min.cheapest_price, "duration", ch_duration_min.cheapest_duration, "[BestDeal] price", bd_price_min.bestdeal_price
            history_csv_file_writer.writerow([ch_price_min.departure_date.strftime('%Y-%m-%d'),
                                                ch_price_min.cheapest_price, ch_price_min.cheapest_duration.toFloat(), ch_price_min.cheapest_duration,
                                                ch_duration_min.cheapest_price, ch_duration_min.cheapest_duration.toFloat(), ch_duration_min.cheapest_duration,
                                                bd_price_min.bestdeal_price, bd_price_min.bestdeal_duration.toFloat(), bd_price_min.bestdeal_duration
                                            ])
        history_csv_file.close()

        history_csv_file = open(history_csv + '_ret.csv', 'wt')
        history_csv_file_writer = csv.writer(history_csv_file, delimiter=',', lineterminator='\n')
        # Write Returns
        history_csv_file_writer.writerow(['Date of return','Cheapest price','Cheapest duration 10','Cheapest duration 60','Quicker price','Quicker duration 10','Quicker duration 60','Best Deal price','Best Deal duration 10','Best Deal duration 60'])
        for everyDepartureList in results_ret:
            ch_price_min = min(everyDepartureList, key=attrgetter('cheapest_price'))
            ch_duration_min = min(everyDepartureList, key=attrgetter('cheapest_duration.totalMinutes'))
            bd_price_min = min(everyDepartureList, key=attrgetter('bestdeal_price'))
            #print "{", ch_price_min.return_date, "} ", "[Cheapest] price", ch_price_min.cheapest_price, "duration", ch_duration_min.cheapest_duration, "[BestDeal] price", bd_price_min.bestdeal_price
            history_csv_file_writer.writerow([ch_price_min.return_date.strftime('%Y-%m-%d'),
                                                ch_price_min.cheapest_price, ch_price_min.cheapest_duration.toFloat(), ch_price_min.cheapest_duration,
                                                ch_duration_min.cheapest_price, ch_duration_min.cheapest_duration.toFloat(), ch_duration_min.cheapest_duration,
                                                bd_price_min.bestdeal_price, bd_price_min.bestdeal_duration.toFloat(), bd_price_min.bestdeal_duration
                                            ])
        history_csv_file.close()
        print 'csv written'
