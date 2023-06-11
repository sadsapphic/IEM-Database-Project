DROP TABLE IF EXISTS main; 

CREATE TABLE IF NOT EXISTS main(
    IEM_name VARCHAR(255) NOT NULL PRIMARY KEY,
    num_of_files INT,
    preference_pct FLOAT,
    average_error_dB FLOAT,
    slope_of_error FLOAT,
    STDEV_of_error FLOAT,
    variance FLOAT,
    highest_Preference_pct FLOAT,
    lowest_preference_pct FLOAT
);

DROP TABLE IF EXISTS avg_measurement_data; 

CREATE TABLE IF NOT EXISTS avg_measurement_data(
    id SERIAL PRIMARY KEY,
    IEM_name VARCHAR(255) NOT NULL,
    x FLOAT,
    y FLOAT,
    FOREIGN KEY(IEM_name) REFERENCES Main(IEM_name)
);


DROP TABLE IF EXISTS measurement_data;

CREATE TABLE IF NOT EXISTS measurement_data( 
    id SERIAL PRIMARY KEY,
    IEM_name VARCHAR(255) NOT NULL, 
    measurement_num INT, 
    X FLOAT,  
    Y FLOAT, 
    contributor VARCHAR(255)
);

DROP TABLE IF EXISTS contributors; 

CREATE TABLE IF NOT EXISTS contributors(
    id SERIAL PRIMARY KEY,
    IEM_name VARCHAR(255) NOT NULL REFERENCES Main(IEM_name), 
    contributor VARCHAR(255),
    credit VARCHAR(255)
);

DROP TABLE IF EXISTS target; 

CREATE TABLE IF NOT EXISTS target(
    id SERIAL PRIMARY KEY,
    X FLOAT, 
    Y FLOAT 
);

DROP TABLE IF EXISTS users; 

CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255), 
    first_name VARCHAR(255)
);
