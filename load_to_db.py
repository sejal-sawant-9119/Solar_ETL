import pandas as pd
from sqlalchemy import create_engine
	
# Create Database Connection
engine = create_engine('sqlite:///solar.db', echo=True)

# Load Cleaned data
df = pd.read_csv('clean_solar_data.csv')
print("Loaded cleaned data:", df.shape)

# Write to SQLite table
df.to_sql('solar_ops', con=engine, if_exists='replace', index=False)
print("Date loaded into solar_ops table in solar_db")