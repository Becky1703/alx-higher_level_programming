-- script lists all shows from database by rating
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;
