SELECT ANIMAL_ID, NAME, CASE 
WHEN SEX_UPON_INTAKE LIKE "%neutered%" OR SEX_UPON_INTAKE LIKE "%spayed%" 
THEN "O" ELSE "X" END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID