-- lists all cities contained in the database hbtn_0d_usa.
SELECT id, name
  FROM cities
WHERE state_id IN
      (SELECT id
        FROM states)
ORDER BY id;
