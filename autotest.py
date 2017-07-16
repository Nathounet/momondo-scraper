from flight import Flight
from shorttime import Time
from copy import deepcopy
from datetime import datetime, timedelta

class AutoTest():
    def __init__(self, results_dep):
        everyReturnCombination = []
        scrapedFlight = Flight()

        scrapedFlight.departure_date = datetime.strptime('29-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('29-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 538
        scrapedFlight.cheapest_duration = Time('15h17m')
        scrapedFlight.bestdeal_price = 604
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('29-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('30-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 524
        scrapedFlight.cheapest_duration = Time('17h15m')
        scrapedFlight.bestdeal_price = 623
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('29-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('31-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 526
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 623
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('29-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('1-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 526
        scrapedFlight.cheapest_duration = Time('16h27m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('29-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('2-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 526
        scrapedFlight.cheapest_duration = Time('16h12m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('29-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('3-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 603
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('29-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('4-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 635
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        results_dep.append(deepcopy(everyReturnCombination))
        everyReturnCombination= []

        scrapedFlight.departure_date = datetime.strptime('30-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('29-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 538
        scrapedFlight.cheapest_duration = Time('16h2m')
        scrapedFlight.bestdeal_price = 604
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('30-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('30-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 526
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 623
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('30-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('31-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 526
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 623
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('30-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('1-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 553
        scrapedFlight.cheapest_duration = Time('14h0m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('30-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('2-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 554
        scrapedFlight.cheapest_duration = Time('22h27m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('30-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('3-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 603
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('30-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('4-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 635
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        results_dep.append(deepcopy(everyReturnCombination))
        everyReturnCombination= []

        scrapedFlight.departure_date = datetime.strptime('31-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('29-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 553
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 604
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('31-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('30-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 526
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 623
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('31-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('31-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 526
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 623
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('31-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('1-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 553
        scrapedFlight.cheapest_duration = Time('14h0m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('31-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('2-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 554
        scrapedFlight.cheapest_duration = Time('22h27m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('31-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('3-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 603
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('31-8-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('4-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 635
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        results_dep.append(deepcopy(everyReturnCombination))
        everyReturnCombination= []

        scrapedFlight.departure_date = datetime.strptime('1-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('29-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 538
        scrapedFlight.cheapest_duration = Time('23h57m')
        scrapedFlight.bestdeal_price = 604
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('1-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('30-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 526
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 623
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('1-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('31-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 526
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 623
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('1-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('1-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 557
        scrapedFlight.cheapest_duration = Time('21h45m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('1-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('2-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 557
        scrapedFlight.cheapest_duration = Time('21h45m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('1-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('3-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 603
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('1-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('4-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 635
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 719
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        results_dep.append(deepcopy(everyReturnCombination))
        everyReturnCombination= []

        scrapedFlight.departure_date = datetime.strptime('2-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('29-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 538
        scrapedFlight.cheapest_duration = Time('16h2m')
        scrapedFlight.bestdeal_price = 667
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('2-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('30-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 526
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 686
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('2-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('31-12-2017', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 470
        scrapedFlight.cheapest_duration = Time('15h15m')
        scrapedFlight.bestdeal_price = 686
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('2-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('1-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 470
        scrapedFlight.cheapest_duration = Time('15h15m')
        scrapedFlight.bestdeal_price = 782
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('2-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('2-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 549
        scrapedFlight.cheapest_duration = Time('16h12m')
        scrapedFlight.bestdeal_price = 782
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('2-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('3-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 603
        scrapedFlight.cheapest_duration = Time('16h17m')
        scrapedFlight.bestdeal_price = 782
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        scrapedFlight.departure_date = datetime.strptime('2-9-2017', '%d-%m-%Y')
        scrapedFlight.return_date = datetime.strptime('4-1-2018', '%d-%m-%Y')
        scrapedFlight.cheapest_price = 634
        scrapedFlight.cheapest_duration = Time('15h15m')
        scrapedFlight.bestdeal_price = 782
        scrapedFlight.bestdeal_duration = Time('12h0m')
        everyReturnCombination.append(deepcopy(scrapedFlight))
        everyReturnCombination= []
