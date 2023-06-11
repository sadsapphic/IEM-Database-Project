COPY Main(IEM_name, num_of_files, preference_pct, average_error_dB, slope_of_error, STDEV_of_error, variance, highest_Preference_pct, lowest_preference_pct )
FROM '/tmp/Main.csv' 
DELIMITER ',' 
CSV HEADER;

COPY avg_measurement_data(IEM_name, X, Y)
FROM '/tmp/avg_measurement_data.csv' 
DELIMITER ',' 
CSV HEADER;

COPY measurement_data(IEM_name, measurement_num, X, Y, contributor)
FROM '/tmp/measurement_data.csv' 
DELIMITER ',' 
CSV HEADER;

COPY contributors(IEM_name, Contributor, credit)
FROM '/tmp/contributors.csv' 
DELIMITER ',' 
CSV HEADER;

COPY target(X, Y)
FROM '/tmp/target.csv' 
DELIMITER ',' 
CSV HEADER;
