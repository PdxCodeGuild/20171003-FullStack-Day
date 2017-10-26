
# Lab 29: Rain Data


The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly:  http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...

```
Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

```

Download one of these files (or the csv I've compiled containing all of them), and write a function to load the file. Each line of the file will become a list or class or tuple consisting of a `datetime` and a series of `int`s.

To parse the dates, use [datetime.striptime](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior). Below I've shown how to parse an example string, resulting in a [datetime](https://docs.python.org/3.6/library/datetime.html#date-objects) object. We can then access the year, month, and day on that datetime as ints.

```python
import datetime
date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(date.year)
print(date.month)
print(date.day)
```

## Version 2

Now that you've successfully extracted the data, let's done some statistics.

Calculate the mean of the data:

![mean](https://wikimedia.org/api/rest_v1/media/math/render/svg/c7740a0aa91314dbf006e8583ce6f61585e3aab6)


Use the mean to calculate the variance:

![variance](https://wikimedia.org/api/rest_v1/media/math/render/svg/0c5c6e7bbd52e69c29e2d5cfe21989313aba55d4)

Find the day which had the most rain.

Find the year which had the most rain on average.


## Version 3

Using `matplotlib` create a chart of the dates and the daily totals for a given year. The `x_values` will be a list of dates, The `y_values` are a list of the daily totals. If you don't have matplotlib installed, run `pip install matplotlib`. You can learn more about matplotlib [here](https://matplotlib.org/2.1.0/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py).

```python
import matplotlib.pyplot as plt
...
plt.plot(x_values, y_values)
plt.show()
```                                                                                         