# harvest records with python pyoaiharvest.py from socialhistoryservices oai between a date range
# example command line command: python pyoaiharvest.py -l https://api.socialhistoryservices.org/solr/all/oai -o export_test_script.xml -m marcxml -f 2023-05-16 -u 2023-05-17
# this script here below makes this command executable from this script, so the parameters can be used as variables and the data be stored in smaller files
# NOTE: it has to be placed in the oai repo harvester to be executed from there (or change the path in subprocess line later...)
# written by Liliana on May 19, 2023, used for harvesting ALL records from the socialhistoryservices oai

#library to run a shell script within a python script (https://earthly.dev/blog/python-subprocess/)
import subprocess
# pandas and pandas libraries to deal with dates and date ranges
import pandas as pd
from datetime import datetime
from pandas.tseries.offsets import DateOffset

# main oai url
url = 'https://api.socialhistoryservices.org/solr/all/oai'
metadata_format = 'marcxml'
start_date = datetime.strptime("2006-12-31", "%Y-%m-%d")
#periods means how many dates you want
start_date_list = pd.date_range(start_date, periods=198, freq="M ")
# loop through start date to create end date and file name (each period of time will have a file name)
for start_date in start_date_list:
	end_date = start_date + DateOffset(months=1)
	# use date range to give the file a name
	file_name = f"{start_date.strftime('%Y-%m-%d')}_{end_date.strftime('%Y-%m-%d')}.xml"
	# execute the command line command replacing the parameters with the variables defined above
	subprocess.run("python pyoaiharvest.py -l %s -o %s -m %s -f %s -u %s" % (url, file_name, metadata_format, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')), shell=True)