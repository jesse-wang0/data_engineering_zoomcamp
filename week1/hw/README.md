- Q1) 24.3.1

Done by executing these commands:

docker run -it python:3.12.8 bash
pip --version


- Q2) db:5432

- Q3) 104802; 198924; 109603; 27678, 35189

``` sql
SELECT COUNT(*)
FROM green_taxi_data
WHERE lpep_dropoff_datetime >= '2019-10-01'
	AND lpep_dropoff_datetime < '2019-11-1'
	AND trip_distance <= 1;

SELECT COUNT(*)
FROM green_taxi_data
WHERE lpep_dropoff_datetime >= '2019-10-01'
	AND lpep_dropoff_datetime < '2019-11-1'
	AND trip_distance > 1
	AND trip_distance <= 3;

SELECT COUNT(*)
FROM green_taxi_data
WHERE lpep_dropoff_datetime >= '2019-10-01'
	AND lpep_dropoff_datetime < '2019-11-1'
	AND trip_distance > 3
	AND trip_distance <= 7;

SELECT COUNT(*)
FROM green_taxi_data
WHERE lpep_dropoff_datetime >= '2019-10-01'
	AND lpep_dropoff_datetime < '2019-11-1'
	AND trip_distance > 7
	AND trip_distance <= 10;

SELECT COUNT(*)
FROM green_taxi_data
WHERE lpep_dropoff_datetime >= '2019-10-01'
	AND lpep_dropoff_datetime < '2019-11-1'
	AND trip_distance > 10;

- Q5) 2019-10-31
SELECT lpep_pickup_datetime, trip_distance
FROM green_taxi_data
WHERE trip_distance = (
    SELECT MAX(trip_distance) FROM green_taxi_data
);

- Q5) East Harlem North, East Harlem South, Morningside Heights
SELECT g."PULocationID", z."Zone", SUM(total_amount)
FROM green_taxi_data g
JOIN zones z ON z."LocationID"=g."PULocationID"
WHERE lpep_pickup_datetime>='2019-10-18' 
	AND lpep_pickup_datetime<'2019-10-19'
GROUP BY g."PULocationID", z."Zone"
HAVING SUM(total_amount) > 13000
ORDER BY sum DESC;

- Q6) East Harlem North
SELECT g."lpep_pickup_datetime", g."tip_amount", z."Zone" as drop_off_zone
FROM green_taxi_data g
JOIN zones z ON z."LocationID"=g."PULocationID"
WHERE g.tip_amount = (
	SELECT MAX(tip_amount)
	FROM green_taxi_data g
	JOIN zones z ON z."LocationID"=g."PULocationID"
	WHERE lpep_pickup_datetime>='2019-10-01' 
		AND lpep_pickup_datetime<'2019-11-01'
		AND z."Zone"='East Harlem North')  



- Q7) terraform init, terraform apply -auto-approve, terraform destroy