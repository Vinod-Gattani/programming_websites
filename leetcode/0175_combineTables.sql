# Write your MySQL query statement below

SELECT
    a.FirstName,
    a.LastName,
    b.City,
    b.State
FROM
    Person a
    left join Address b on a.PersonId = b.PersonId
    
'''
{"headers": {"Person": ["PersonId", "LastName", "FirstName"], "Address": ["AddressId", "PersonId", "City", "State"]}, "rows": {"Person": [[1, "Wang", "Allen"]], "Address": [[1, 2, "New York City", "New York"]]}}

{"headers": ["FirstName", "LastName", "City", "State"], "values": [["Allen", "Wang", null, null]]}
'''