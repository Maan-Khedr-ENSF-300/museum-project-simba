USE museum;

-- TASK 1: Show all tables and explain how they are realted 
SHOW tables;
DESCRIBE artobject;
DESCRIBE painting;
DESCRIBE sculpture;
DESCRIBE statue;
DESCRIBE other;
DESCRIBE permanent;
DESCRIBE borrowed;
DESCRIBE artist;
DESCRIBE collection;
DESCRIBE exhibition;


-- TASK 2: A basic retrieval query
Select Name, DateBorn, DateDied, MainStyle, 
Description
From artist 
Where Country ="France";


-- TASK 3: A retrieval query with ordered results 
SELECT artist.Name, artist.Country, artist.MainStyle, artist.DateBorn
FROM Artist 
WHERE Artist.DateBorn
ORDER BY Artist.DateBorn;


-- TASK 4: A nested retrieval query
SELECT Sculpture.IDNum, Sculpture.Material, Sculpture.Height, Sculpture.Weight, Sculpture.Style
FROM Sculpture
WHERE Sculpture.Style IN
(SELECT Style FROM Statue
WHERE Style = 'Roman');


-- TASK 5: A retrieval query using joined tables
SELECT Permanent.IDNum, Permanent.PaintingStatus, Permanent.Cost
FROM Permanent
RIGHT JOIN Statue
ON Permanent.IDNum = Statue.IDNum;


-- TASK 6: An update operation with any necessary triggers 
UPDATE Permanent
SET Cost = Cost * 100
WHERE PaintingStatus = 'On Display';


-- TASK 7: A deletion operation with any necessary triggers 
USE museum;
DELETE FROM Borrowed 
WHERE Collection = 'MasterPieces of The Louvre';

