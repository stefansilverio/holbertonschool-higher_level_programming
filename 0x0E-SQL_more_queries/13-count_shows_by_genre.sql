-- tv shows that only contain
-- sort in ascending order
SELECT `tv_genres`.`name`, COUNT(*) number_of_shows FROM `tv_genres`
       INNER JOIN `tv_show_genres` ON
       `tv_genres`.`id` = `tv_show_genres`.`genre_id` GROUP BY
       `tv_genres`.`name` ORDER BY `number_of_shows` DESC;
