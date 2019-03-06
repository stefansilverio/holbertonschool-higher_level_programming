-- show all shows in database
-- return NULL if not exist
SELECT `tv_shows`.`title`, `tv_show_genres`.`genre_id` FROM `tv_shows`
        LEFT OUTER JOIN `tv_show_genres` ON `tv_shows`.`id`
	 = `tv_show_genres`.`show_id` WHERE `tv_show_genres`.`show_id`
	 IS NULL OR `tv_show_genres`.`show_id` IS NOT NULL
	 ORDER BY `tv_shows`.`title` ASC, `tv_show_genres`.`genre_id` ASC;
