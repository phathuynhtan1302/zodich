import pandas as pd
from datetime import datetime

#Functions
def convert_date_format(date_str):
  """Converts a date string from DD.MM.YYYY to DD/MMM/YYYY format."""
  date_obj = datetime.strptime(date_str, '%d.%m.%Y')
  return date_obj.strftime('%d/%b/%Y')

# Read .csv file
columns_to_read = ['Waybill Number','Shipment Date','Shipment Reference','Recipient Name','Recipient City','Recipient ZIP/Postal Code','Recipient Country','Item Description']
df = pd.read_csv('./Input/shipments.csv',usecols=columns_to_read)

# Add new columns
df['Person Key In'] = 'Louis'
df['Origin Country'] = ''
df['MONTH'] = ''
df['Current Date'] = '=TODAY()'
df['Aging Bucket'] = ''
df['Zone'] = ''
df['State (key for MY if N/A)'] = ''

# Rename Columns
df.rename(columns={'Shipment Date': 'Date Shipped (MM/DD)'}, inplace=True)
df.rename(columns={'Recipient Name': 'Customer Name'}, inplace=True)
df.rename(columns={'Recipient ZIP/Postal Code': 'Recipient ZIP Code'}, inplace=True)
df.rename(columns={'Waybill Number': 'Tracking Number'}, inplace=True)
df.rename(columns={'Recipient Country': 'Shipped Country'}, inplace=True)

# Processing data
df['Shipment Reference'] = df['Shipment Reference'].str.split('/').str[0].str.strip()
df['Date Shipped (MM/DD)'] = df['Date Shipped (MM/DD)'].apply(convert_date_format)

# Re-order datafram
df = df[['Person Key In','Date Shipped (MM/DD)','Origin Country','Shipped Country','MONTH','Current Date','Aging Bucket','Shipment Reference','Customer Name','Recipient City','Recipient ZIP Code','Tracking Number','Zone','State (key for MY if N/A)','Item Description']]

# Write to Output file
df.to_csv('./Output/shipments_process.csv', index=False)

print(df)