from pytrends.request import TrendReq
import pytrends
import matplotlib.pyplot as plt
import pandas as pd

#*************WE MUST CHANGE THE VARIABLE BELOW TO SPECIFY OUR SEARCH TERMS******************
search_terms = ["climate change", "global warming"]
timeframe = "2012-01-01 2020-08-01"

pytrends = TrendReq(hl='en-US', tz=360)

#building payload
pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(search_terms,
                       timeframe=timeframe)
trends = pytrends.interest_over_time()

#pandas df for this
trends.tail()

if all(trends.isPartial == False):
    del trends['isPartial']

def plot_searchterms(df):
    """Plots google trends

    Parameters
    ----------
    df: pandas dataframe
        As returned from pytrends, without the "isPartial" column

    Returns
    -------
    ax: axis handle
    """
    fig = plt.figure(figsize = (15,8))
    ax = fig.add_subplot(111)
    df.plot(ax=ax)
    plt.ylabel('Relative search term frequency')
    plt.xlabel('Date')
    plt.ylim((0,120))
    plt.legend(loc='lower left')
    return ax

plt.style.use('ggplot')
ax = plot_searchterms(trends)
plt.show()

