SQLAlchemy Homework - Surfs Up!
Precipitation Analysis
1.	Design a query to retrieve the last 12 months of precipitation data.
The query results the last date in the dataset is 2017-08-23, twelve months from there is 2016-08-23
2.	Load the query results into a Pandas DataFrame and set the index to the date column.
The DataFrame shows 2,230 rows and 1 column as the first column was set as index, thus it does count as a data column.
3.	Sort the DataFrame values by date.
Sorted DataFrame shows in ascending order with date 2016-08-23 as the first row and 2017-08-23 as the last row
4.	Plot the results using the DataFrame plot method.
 



Station Analysis
1.	Design a query to calculate the total number of stations.
The query calculated 9 stations in the dataset.
2.	Design a query to find the most active stations.
o	List the stations and observation counts in descending order.
[('USC00519281', 'WAIHEE 837.5, HI US', 2772),
('USC00519397', 'WAIKIKI 717.2, HI US', 2724),
('USC00513117', 'KANEOHE 838.1, HI US', 2709),
('USC00519523', 'WAIMANALO EXPERIMENTAL FARM, HI US', 2669),
('USC00516128', 'MANOA LYON ARBO 785.2, HI US', 2612),
('USC00514830', 'KUALOA RANCH HEADQUARTERS 886.9, HI US', 2202),
('USC00511918', 'HONOLULU OBSERVATORY 702.2, HI US', 1979),
('USC00517948', 'PEARL CITY, HI US', 1372),
('USC00518838', 'UPPER WAHIAWA 874.3, HI US', 511)]
o	Which station has the highest number of observations?
The highest number of temperature observations (most active) station is: WAIHEE 837.5, HI US, station ID: USC00519281. Recorded 2,772 records
3.	Design a query to retrieve the last 12 months of temperature observation data (TOBS).
o	Filter by the station with the highest number of observations.
Query results WAIHEE 837.5, HI US Station ID: USC00519281 is the station with the highest number of observations, recorded 2,772 records
o	Plot the results as a histogram with bins=12. 
