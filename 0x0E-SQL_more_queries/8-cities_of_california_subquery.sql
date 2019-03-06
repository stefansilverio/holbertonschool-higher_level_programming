-- list all cities in CA in database
-- sorted in ascending order
SELECT `id`, `name` FROM cities WHERE `cities`.`state_id` =
       (SELECT `id` FROM `states` WHERE `name` = 'California');
