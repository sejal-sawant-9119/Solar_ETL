import pandas as pd

def clean_solar_data(file_path):
	df = pd.read_csv(file_path)
	df.dropna(subset=['SSE_ID'], inplace=True)
	df['Installation_Date'] = pd.to_datetime(df['Installation_Date'], errors='coerce')	
	df.dropna(subset=['Installation_Date'], inplace=True)
	df['Year'] = pd.DatetimeIndex(df['Installation_Date']).year
	df.drop_duplicates(inplace=True)
	return df

if __name__ =="__main__":
	df = clean_solar_data('sample_solar_data.csv')
	df.to_csv('clean_solar_data.csv', index=False)
	print("Cleaned data saved to clean_solar_data.csv")