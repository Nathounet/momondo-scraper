from operator import attrgetter
from plotly.graph_objs import *
import plotly.plotly as plotlyb
import plotly.offline as plotoff
import plotly.dashboard_objs as plotdash


class Plot():
    def __init__(self, config_parameters):
        # Fixed

        self.search_id = dep_date_min.strftime('%d-%m') + '_' + ret_date_max.strftime('%d-%m-%Y') + '_' + config_parameters.departure + '_' + config_parameters.arrival


def plot():
    dates = []
    price_cheapest = []
    price_quickest = []
    price_bestdeal = []
    duration_cheapest = []
    duration_quickest = []
    duration_bestdeal = []

    for everyDepartureList in results_ret:
        ch_price_min = min(everyDepartureList, key=attrgetter('cheapest_price'))
        ch_duration_min = min(everyDepartureList, key=attrgetter('cheapest_duration.totalMinutes'))
        bd_price_min = min(everyDepartureList, key=attrgetter('bestdeal_price'))

        dates.append(ch_price_min.arrival.strReverse())
        price_cheapest.append(ch_price_min.cheapest_price)
        price_quickest.append(ch_duration_min.cheapest_price)
        price_bestdeal.append(bd_price_min.bestdeal_price)
        duration_cheapest.append(ch_price_min.cheapest_duration.toFloat())
        duration_quickest.append(ch_duration_min.cheapest_duration.toFloat())
        duration_bestdeal.append(bd_price_min.bestdeal_duration.toFloat())

    price_max = max(price_cheapest + price_quickest + price_bestdeal)
    price_min = min(price_cheapest + price_quickest + price_bestdeal)
    price_range = [int(price_min - (price_max - price_min)/4), int(price_max + (price_max - price_min)/4)]

    plotlyb.sign_in('Nathounet91', 'sMEVUzlsCFUhPNtBT3ag')
    trace1 = {
      "x": dates,
      "y": price_cheapest,
      "name": "Cheapest price",
      "showlegend": False,
      "text": duration_cheapest,
      "type": "bar",
      "xaxis": "x",
      "yaxis": "y"
    }
    trace2 = {
      "x": dates,
      "y": price_quickest,
      "name": "Quicker price",
      "showlegend": False,
      "text": duration_quickest,
      "type": "bar",
      "xaxis": "x",
      "yaxis": "y"
    }
    trace3 = {
      "x": dates,
      "y": price_bestdeal,
      "name": "BestDeal price",
      "showlegend": False,
      "text": duration_bestdeal,
      "type": "bar",
      "xaxis": "x",
      "yaxis": "y"
    }
    trace4 = {
      "x": dates,
      "y": duration_cheapest,
      "line": {"color": "rgb(31, 119, 180)"},
      "mode": "lines+markers",
      "name": "Cheapest duration",
      "showlegend": False,
      "text": price_cheapest,
      "type": "scatter",
      "xaxis": "x",
      "yaxis": "y2"
    }
    trace5 = {
      "x": dates,
      "y": duration_quickest,
      "line": {"color": "rgb(255, 127, 14)"},
      "mode": "lines+markers",
      "name": "Quicker duration",
      "showlegend": False,
      "text": price_quickest,
      "type": "scatter",
      "visible": True,
      "xaxis": "x",
      "yaxis": "y2"
    }
    trace6 = {
      "x": dates,
      "y": duration_bestdeal,
      "connectgaps": False,
      "line": {"color": "rgb(44, 160, 44)"},
      "mode": "lines+markers",
      "name": "BestDeal duration",
      "showlegend": False,
      "text": price_bestdeal,
      "type": "scatter",
      "xaxis": "x",
      "yaxis": "y2",
    }
    data = Data([trace1, trace2, trace3, trace4, trace5, trace6])
    layout = {
      "autosize": True,
      "dragmode": "zoom",
      "hovermode": "closest",
      "legend": {
        "orientation": "v",
        "traceorder": "reversed"
      },
      "margin": {
        "r": 40,
        "t": 0,
        "b": 60,
        "l": 65
      },
      "showlegend": False,
      "xaxis": {
        "title": "<b>Date of departure</b>",
        "anchor": "y",
        "autorange": True,
        "domain": [-0.01, 1.01],
        "gridcolor": "rgb(182, 76, 76)",
        "mirror": False,
        "showgrid": False,
        "showline": False,
        "showticklabels": True,
        "side": "bottom",
        "ticks": "",
        "type": "date",
        "zeroline": False,
      },
      "yaxis": {
        "title": "<b>Price</b>",
        "anchor": "x",
        "autorange": False,
        "domain": [-0.01, 0.61],
        "fixedrange": True,
        "range": price_range,
        "showgrid": True,
        "showline": False,
        "ticks": "",
        "type": "linear",
        "zeroline": True,
        "zerolinecolor": "rgba(238, 238, 238, 0.93)"
      },
      "yaxis2": {
        "title": "<b>Duration</b>",
        "anchor": "x",
        "autorange": True,
        "domain": [0.61, 1.01],
        "type": "linear"
      }
    }
    fig = Figure(data=data, layout=layout)

    plot_url = plotlyb.plot(fig, auto_open=False, filename=search_id+'_returns')

    plotoff.offline.plot(fig, auto_open=False)

    dash(plot_url)


def fileId_from_url(url):
    """Return fileId from a url."""
    index = url.find('~')
    fileId = url[index + 1:]
    local_id_index = fileId.find('/')
    return fileId.replace('/', ':')


def dash(url_1):


    my_dboard = plotdash.Dashboard()
    my_dboard.get_preview()


    fileId_1 = fileId_from_url(url_1)
    #fileId_2 = fileId_from_url(url_2)
    test = url_1.split('~')[1].replace('/', ':')
    print fileId_1, test

    box_a = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': fileId_1,
        'title': 'scatter-for-dashboard'
    }

    #box_c = {
    #    'type': 'box',
    #    'boxType': 'plot',
    #    'fileId': fileId_2,
    #    'title': 'box-for-dashboard',
    #    'shareKey': sharekey_from_url(url_2)
    #}

    my_dboard.insert(box_a)
    my_dboard.get_preview()

    plotdash.upload(my_dboard, 'My First Dashboard with Python')
