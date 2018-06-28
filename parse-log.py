import urllib.request
import pandas as pd
import re
from datetime import datetime
import pytz
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('max_columns',10)

def parse_str(x):
    """
    Returns the string delimited by two characters.

    Example:
        `>>> parse_str('[my string]')`
        `'my string'`
    """
    return x[1:-1]

def parse_datetime(x):
    '''
    Parses datetime with timezone formatted as:
        `[day/month/year:hour:minute:second zone]`

    Example:
        `>>> parse_datetime('13/Nov/2015:11:45:42 +0000')`
        `datetime.datetime(2015, 11, 3, 11, 45, 4, tzinfo=<UTC>)`

    Due to problems parsing the timezone (`%z`) with `datetime.strptime`, the
    timezone will be obtained using the `pytz` library.
    '''
    dt = datetime.strptime(x[1:-7], '%d/%b/%Y:%H:%M:%S')
    dt_tz = int(x[-6:-3])*60+int(x[-3:-1])
    return dt.replace(tzinfo=pytz.FixedOffset(dt_tz))

# data = pd.read_csv(StringIO(accesslog))
url = "http://www.cs.tufts.edu/comp/116/access.log"
accesslog =  urllib.request.urlopen(url).read().decode('utf-8')
fields = ['host', 'identity', 'user', 'time_part1', 'time_part2', 'cmd_path_proto', 
          'http_code', 'response_bytes', 'referer', 'user_agent', 'unknown']
    
data: pd.DataFrame = pd.read_csv(url, sep=' ', header=None, names=fields, na_values=['-'])

# Panda's parser mistakenly splits the date into two columns, so we must concatenate them
time = data.time_part1 + data.time_part2
time_trimmed = time.map(lambda s: re.split('[-+]', s.strip('[]'))[0]) # Drop the timezone for simplicity
data['time'] = pd.to_datetime(time_trimmed, format='%d/%b/%Y:%H:%M:%S')

data.head()

def correlation_plot():
    data.corr() # first calculate correlation between all columns!
    f, ax = plt.subplots(figsize=(11, 9)) # Set up the matplotlib figure
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(data.corr(), mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

def bucket_by_time():
    print(data.reset_index().set_index('time').resample('12h').mean())

def show_plots():
    data.hist()
    
# bucket_by_time()
# show_plots()    


# Split column `cmd_path_proto` into three columns, and decode the URL (ex: '%20' => ' ')
#data['command'], data['path'], data['protocol'] = zip(*data['cmd_path_proto'].str.split().tolist())
#data['path'] = data['path'].map(lambda s: unquote(s))

