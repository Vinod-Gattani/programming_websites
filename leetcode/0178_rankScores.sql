# Write your MySQL query statement below

SELECT
    Score,
    DENSE_RANK() OVER (ORDER BY Score DESC) as "Rank"
FROM
    Scores
    
    
'''
{"headers": {"Scores": ["Id", "Score"]}, "rows": {"Scores": [[1, 3.50], [2, 3.65], [3, 4.00], [4, 3.85], [5, 4.00], [6, 3.65]]}}

{"headers": ["Score", "Rank"], "values": [[4.00, 1], [4.00, 1], [3.85, 2], [3.65, 3], [3.65, 3], [3.50, 4]]}

'''