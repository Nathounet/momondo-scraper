### Libraries
from operator import attrgetter
from plotly.graph_objs import *
import plotly.plotly as plotlyb
import plotly.offline as plotoff
import plotly.dashboard_objs as plotdash
import plotly.exceptions as plotex

### Custom modules
from url import URL

#TODO: create and display average price

class Plot():
    def __init__(self, config_parameters, results_dep, results_ret):
        self.account = True
        self.search_id = (config_parameters.dep_date_min.strftime('%d-%m')
                        + '_' + config_parameters.ret_date_max.strftime('%d-%m-%Y')
                        + '_' + config_parameters.departure
                        + '_' + config_parameters.arrival)
        self.userSignIn()

        self.createDataList(results_dep)
        self.createFigure('Departure')
        self.url_dep = self.sendPlot('_departures')

        self.createDataList(results_ret)
        self.createFigure('Return')
        self.url_ret = self.sendPlot('_returns')

        #self.url_hist = self.plot(history) #TODO: add cheapest fare history below both, from csv

        url_momondo = URL(config_parameters)
        url_momondo.setDates(
                    config_parameters.dep_date_min.strftime('%d-%m-%Y'),
                    config_parameters.ret_date_max.strftime('%d-%m-%Y'))
        self.updateDashboard(url_momondo.getFullUrl())


    def userSignIn(self):
        if self.account == True:
            plotlyb.sign_in('Nathounet91', 'sMEVUzlsCFUhPNtBT3ag')
            print 'Signed-in as Nathounet91'
        else:
            plotlyb.sign_in('testScrapper', 'nn4kOOGlmvhfkKGzAoyJ')
            print 'Signed-in as testScrapper'
        self.account = not self.account


    def createFigure(self, way):
        self.createTraces(way)
        self.createLayout(way)

        self.figure_plot = Figure(data=self.trace_data_plot, layout=self.layout_plot)
        #plotoff.offline.plot(fig, auto_open=False)


    def sendPlot(self, way):
        try:
            url = plotlyb.plot(self.figure_plot, auto_open=False, filename=self.search_id+way)
        except plotex.PlotlyRequestError:
            print 'plot.ly API calls reached, switching account'
            self.userSignIn()
            url = plotlyb.plot(self.figure_plot, auto_open=False, filename=self.search_id+way)
        return url


    def createDataList(self, results):
        self.data_dict = {}
        self.data_dict['cheapest'] = {'date':[], 'date_otherway':[], 'price':[], 'duration':[]}
        self.data_dict['quickest'] = {'date':[], 'date_otherway':[], 'price':[], 'duration':[]}
        self.data_dict['bestdeal'] = {'date':[], 'date_otherway':[], 'price':[], 'duration':[]}

        for list_flight in results:
            #TODO: when multiple Flights have the same lowest price return the one with the minimum duration
            ch_price_min = min(list_flight, key=attrgetter('cheapest_price'))
            ch_duration_min = min(list_flight, key=attrgetter('cheapest_duration.totalMinutes'))
            bd_price_min = min(list_flight, key=attrgetter('bestdeal_price'))

            self.data_dict['cheapest']['date'].append(ch_price_min.date_this_way.strftime('%Y-%m-%d'))
            self.data_dict['cheapest']['date_otherway'].append(ch_price_min.date_other_way.strftime('%b %d, %Y'))
            self.data_dict['cheapest']['price'].append(ch_price_min.cheapest_price)
            self.data_dict['cheapest']['duration'].append(ch_price_min.cheapest_duration.toFloat())

            self.data_dict['quickest']['date'].append(ch_duration_min.date_this_way.strftime('%Y-%m-%d'))
            self.data_dict['quickest']['date_otherway'].append(ch_duration_min.date_other_way.strftime('%b %d, %Y'))
            self.data_dict['quickest']['price'].append(ch_duration_min.cheapest_price)
            self.data_dict['quickest']['duration'].append(ch_duration_min.cheapest_duration.toFloat())

            self.data_dict['bestdeal']['date'].append(bd_price_min.date_this_way.strftime('%Y-%m-%d'))
            self.data_dict['bestdeal']['date_otherway'].append(bd_price_min.date_other_way.strftime('%b %d, %Y'))
            self.data_dict['bestdeal']['price'].append(bd_price_min.bestdeal_price)
            self.data_dict['bestdeal']['duration'].append(bd_price_min.bestdeal_duration.toFloat())

        price_max = max(self.data_dict['cheapest']['price'] + self.data_dict['quickest']['price'] + self.data_dict['bestdeal']['price'])
        price_min = min(self.data_dict['cheapest']['price'] + self.data_dict['quickest']['price'] + self.data_dict['bestdeal']['price'])
        self.data_dict['price_range'] = [int(price_min - (price_max - price_min)/4), int(price_max + (price_max - price_min)/4)]


    def createTraces(self, way):
        # Sign for hover
        if way == 'Departure':
            sign = '< '
        else: #way == 'Return':
            sign = '> '

        price_ch = {
          "x": self.data_dict['cheapest']['date'],
          "y": self.data_dict['cheapest']['price'],
          "name": "Cheapest price",
          "showlegend": False,
          "text": [
                    sign+str(info).replace('\'', '').replace('(', '').replace(')', '') for info
                    in zip(self.data_dict['cheapest']['date_otherway'], self.data_dict['cheapest']['duration'])
                  ],
          "type": "bar",
          "xaxis": "x",
          "yaxis": "y"
        }
        price_qu = {
          "x": self.data_dict['quickest']['date'],
          "y": self.data_dict['quickest']['price'],
          "name": "Quicker price",
          "showlegend": False,
          "text": [
                    sign+str(info).replace('\'', '').replace('(', '').replace(')', '') for info
                    in zip(self.data_dict['quickest']['date_otherway'], self.data_dict['quickest']['duration'])
                  ],
          "type": "bar",
          "xaxis": "x",
          "yaxis": "y"
        }
        price_bd = {
          "x": self.data_dict['bestdeal']['date'],
          "y": self.data_dict['bestdeal']['price'],
          "name": "BestDeal price",
          "showlegend": False,
          "text": [
                    sign+str(info).replace('\'', '').replace('(', '').replace(')', '') for info
                    in zip(self.data_dict['bestdeal']['date_otherway'], self.data_dict['bestdeal']['duration'])
                  ],
          "type": "bar",
          "xaxis": "x",
          "yaxis": "y"
        }
        duration_ch = {
          "x": self.data_dict['cheapest']['date'],
          "y": self.data_dict['cheapest']['duration'],
          "line": {"color": "rgb(31, 119, 180)"},
          "mode": "lines+markers",
          "name": "Cheapest duration",
          "showlegend": False,
          "text": [ sign+str(info).replace('\'', '').replace('(', '').replace(')', '') for info
                    in zip(self.data_dict['cheapest']['date_otherway'], self.data_dict['cheapest']['price']) ],
          "type": "scatter",
          "xaxis": "x",
          "yaxis": "y2"
        }
        duration_qu = {
          "x": self.data_dict['quickest']['date'],
          "y": self.data_dict['quickest']['duration'],
          "line": {"color": "rgb(255, 127, 14)"},
          "mode": "lines+markers",
          "name": "Quicker duration",
          "showlegend": False,
          "text": [ sign+str(info).replace('\'', '').replace('(', '').replace(')', '') for info
                    in zip(self.data_dict['quickest']['date_otherway'], self.data_dict['quickest']['price']) ],
          "type": "scatter",
          "visible": True,
          "xaxis": "x",
          "yaxis": "y2"
        }
        duration_bd = {
          "x": self.data_dict['bestdeal']['date'],
          "y": self.data_dict['bestdeal']['duration'],
          "connectgaps": False,
          "line": {"color": "rgb(44, 160, 44)"},
          "mode": "lines+markers",
          "name": "BestDeal duration",
          "showlegend": False,
          "text": [ sign+str(info).replace('\'', '').replace('(', '').replace(')', '') for info
                    in zip(self.data_dict['bestdeal']['date_otherway'], self.data_dict['bestdeal']['price']) ],
          "type": "scatter",
          "xaxis": "x",
          "yaxis": "y2",
        }
        self.trace_data_plot = Data([price_ch, price_qu, price_bd, duration_ch, duration_qu, duration_bd])


    def createLayout(self, way):
        self.layout_plot = {
          "autosize": True,
          "dragmode": "zoom",
          "hovermode": "closest",
          "legend": {
            "orientation": "v",
            "traceorder": "reversed"
          },
          "margin": {
            "r": 20,
            "t": 0,
            "b": 60,
            "l": 65
          },
          "showlegend": False,
          "xaxis": {
            "title": "<b>Date of "+way+"</b>",
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
            "range": self.data_dict['price_range'],
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


    def updateDashboard(self, url_momondo):
        dboard = plotdash.Dashboard()

        fileId_dep = self.url_dep.split('~')[1].replace('/', ':')
        box_dep = {
            'type': 'box',
            'boxType': 'plot',
            'fileId': fileId_dep,
            'title': 'Departure flights'
        }
        dboard.insert(box_dep)

        fileId_ret = self.url_ret.split('~')[1].replace('/', ':')
        box_ret = {
            'type': 'box',
            'boxType': 'plot',
            'fileId': fileId_ret,
            'title': 'Return flights'
        }
        dboard.insert(box_ret, 'right', 1)

        dboard['layout']['size'] = 520
        dboard['layout']['sizeUnit'] = 'px'
        dboard['settings']['title'] = 'Scrapped flights from '+self.search_id.split('_')[-2]+' to '+self.search_id.split('_')[-1]
        dboard['settings']['logoUrl'] = 'https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Momondo_A-S_logo.svg/1280px-Momondo_A-S_logo.svg.png'
        dboard['settings']['links'] = [{'title': 'See more on Momondo', 'url': url_momondo}]

        plotlyb.dashboard_ops.upload(dboard, filename=self.search_id+'_dashboard')
