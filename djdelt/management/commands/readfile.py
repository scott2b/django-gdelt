import csv
from io import BytesIO, TextIOWrapper
from urllib import request
from zipfile import ZipFile

url = 'http://data.gdeltproject.org/gdeltv2/20180419011500.gkg.csv.zip'

with ZipFile(BytesIO(request.urlopen(url).read())) as zf:
    f = zf.namelist()[0]
    with zf.open(f, 'r') as csvfile:
        reader = csv.reader(TextIOWrapper(csvfile))
        for row in reader:
            print(row)

