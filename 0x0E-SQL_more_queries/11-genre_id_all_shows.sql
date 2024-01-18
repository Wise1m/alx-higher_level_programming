-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT t.title, IFNULL(g.genre_id, NULL) AS genre_id
        FROM tv_shows AS t
        LEFT JOIN tv_show_genres AS g
        ON g.show_id=t.id
ORDER BY t.title, g.genre_id ASC;
