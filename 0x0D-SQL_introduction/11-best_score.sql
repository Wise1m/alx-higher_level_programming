-- lists all records with a score >= 10 in the table of the database  in your MySQL server.
SELECT score, name FROM `second_table` WHERE score >= '10'
ORDER BY score DESC;