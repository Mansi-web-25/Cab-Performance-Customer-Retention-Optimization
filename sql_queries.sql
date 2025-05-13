-- Total rides per user
SELECT user_id, COUNT(*) as ride_count
FROM trips
GROUP BY user_id;

-- Average rating per user
SELECT user_id, AVG(rating) as avg_rating
FROM trips
GROUP BY user_id;

-- Churn identification
SELECT user_id,
       MAX(ride_date) as last_ride_date,
       CASE 
           WHEN MAX(ride_date) < DATE_SUB(CURDATE(), INTERVAL 30 DAY) THEN 1
           ELSE 0
       END AS churned
FROM trips
GROUP BY user_id;
