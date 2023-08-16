-- lists all shows contained in hbtn_0d_tvshows without a genre linked


SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genre ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IN NULL
ORDER BY title, tv_show_genres.genre_id;
