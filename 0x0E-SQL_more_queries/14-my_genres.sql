-- list all genres of show Dexter
-- sort in ascending order
SELECT `name` FROM `tv_genres` INNER JOIN `tv_show_genres`
       ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
       INNER JOIN `tv_shows` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
       WHERE `tv_shows`.`title` = 'Dexter' GROUP BY `tv_shows`.`title`,
       `tv_genres`.`name`;
