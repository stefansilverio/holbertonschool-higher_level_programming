-- list all cities contained in database
-- use the join command
SELECT `cities`.`id`, `cities`.`name`, `states`.`name` FROM `cities`
       INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`;
