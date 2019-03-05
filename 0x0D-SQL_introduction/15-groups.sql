-- list num records with same score
-- display score and num of records w/ score
SELECT `score`, COUNT(*) number FROM second_table GROUP BY `score` ORDER BY
       `number` DESC;
