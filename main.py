import statistics
import pandas
import random
import plotly.figure_factory as ff

df = pandas.read_csv("data.csv")
e = df["reading_time"].tolist()

pm = statistics.mean(e)

def f1():
    thing = []
    for i in range(0, 30):
        thing2 = random.randint(1, 6508)
        value = e[thing2]
        thing.append(value)
    meanofthing = statistics.mean(thing)
    return meanofthing

def f2(blah):
    eeeeee = blah
    fig = ff.create_distplot([eeeeee], ["E"], show_hist=False)
    fig.show()


def setup():
    thing3 = []
    for i in range(0, 100):
        eeeeeeeeeeeeeeeeeeeeeeeeee = f1()
        thing3.append(eeeeeeeeeeeeeeeeeeeeeeeeee)


    f2(thing3)
    
setup()