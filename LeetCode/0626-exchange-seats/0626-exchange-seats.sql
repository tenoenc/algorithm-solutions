SELECT 
    (CASE
        WHEN id % 2 = 1 AND id < s2.cnt THEN id + 1
        WHEN id % 2 = 1 AND id = s2.cnt THEN id
        ELSE id - 1
    END) AS id,
    student
FROM Seat s1,
    (SELECT COUNT(*) AS cnt FROM Seat) s2
ORDER BY id ASC;