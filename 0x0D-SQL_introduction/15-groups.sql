-- list num records with same score
-- display score and num of records w/ score
SELECT `score` number COUNT(*) FROM second_table HAVING COUNT(*) > 1;
