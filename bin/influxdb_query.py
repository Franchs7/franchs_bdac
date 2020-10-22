from influxdb import DataFrameClient

client = DataFrameClient(host='127.0.0.1', port=8086,username='root', password='root', database='NOAA_water_database')
query = 'select * from h2o_temperature;'
res = client.query(query,chunked=False)
data = res['h2o_temperature']
print(data.groupby('location', axis=0).resample('30min').sum())
