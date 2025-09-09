SELECT 
    week,
    COUNT(DISTINCT user_id) as active_users,
    (SELECT COUNT(*) FROM retention_users) as total_users,
    ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(*) FROM retention_users), 3) as retention_percentage
FROM (
    SELECT 
        r.user_id,
        EXTRACT(WEEK FROM ra.date) - EXTRACT(WEEK FROM r.registration_date) as week
    FROM retention_users r
    JOIN retention_users_activity ra ON r.user_id = ra.user_id
) active
WHERE week > 0
GROUP BY week
ORDER BY week