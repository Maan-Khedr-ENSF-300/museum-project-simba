DROP DATABASE IF EXISTS Museum;
CREATE DATABASE Museum; 
USE Museum;

CREATE TABLE IF NOT EXISTS ArtObject (
	IDNum					integer,
	Artist					varchar(30),
	Year					integer,
    Title					varchar(30),
    Origin					varchar(30),
    Description				varchar(30),
    Epoch					varchar(30),
    Category				varchar(30),
    Ownership				varchar(30),
	primary key (IDNum)
);

INSERT INTO ArtObject
VALUES
(1, 'Benedetto da Rovezzano', 1524, 'Angel Bearing Candlestick', 'Egypt', null, 'Renaissance', 'Sculpture', 'Owned'),
(2, 'Benedetto da Rovezzano', 1529, 'Angel Bearing Candlestick', 'Egypt', null, 'Renaissance', 'Sculpture', 'Owned'),
(3, 'George Gower', 1567, 'The Hampden Portrait', 'Italy', null, 'Ancient Period', 'Painting', 'Owned'),
(4, 'Hans Holbein', 1537, 'Henry VIII', 'Egypt', null, 'Renaissance', 'Painting', 'Owned'),
(5, 'Hans Holbein', 1511, 'Armor Garniture', 'Italy', null, 'Renaissance', 'Statue', 'Owned'),
(6, 'George Gower', 1580, 'Fencing Doublet', 'Italy', null, 'Ancient Period', 'Statue', 'Owned'),
(7, 'Master of Claude', 1514, 'Book of Hours', 'Egypt', null, 'Baroque Period', 'Other', 'Owned'),
(8, 'Lucas Horenbout', 1544, 'Acts of the Apostles', 'Egypt', null, 'Baroque Period', 'Other', 'Owned'),
(9, 'Antonio Leonelli', 1510, 'Still Life', 'Italy', null, 'Renaissance', 'Painting', 'Owned'),
(10, 'Pablo Picasso', 1912, 'The Scallop', 'Greece', null, 'Realistic Period', 'Painting', 'Owned'),
(11, 'Georges Braque', 1909, 'Violin and Palette', 'Greece', null, 'Realistic Period', 'Painting', 'Owned'),
(12, 'Juan Gris', 1913, 'Violin and Engraving', 'Egypt', null, 'Realistic Period', 'Painting', 'Owned'),
(13, 'Marcos Correa', 1673, 'Trompe l Oeil', 'Greece', null, 'Renaissance', 'Painting', 'Owned'),
(14, 'Pablo Picasso', 1914, 'The Absinthe Glass', 'Greece', null, 'Realistic Period', 'Sculpture', 'Owned'),
(15, 'Jean-Baptiste Carpeaux', 1867, 'Study of a Woman Kneeling', 'France', null, 'Realistic Period', 'Sculpture', 'Owned'),
(16, 'Jean-Baptiste Carpeaux', 1873, 'Why Born Enslaved!', 'Egypt', null, 'Realistic Period', 'Sculpture', 'Owned'),
(17, 'Cristoforo Stati', 1601, 'Orpheus', 'France', null, 'Renaissance', 'Statue', 'Owned'),
(18, 'Giovanni Caccini', 1608, 'Temperance', 'France', null, 'Renaissance', 'Statue', 'Owned'),
(19, 'Cristoforo Solari', 1524, 'Saint Catherine of Alexandria', 'Egypt', null, 'Renaissance', 'Statue', 'Owned'),
(20, 'Antonio Canova', 1822, 'Perseus', 'France', null, 'Romantic Period', 'Statue', 'Owned'),
(21, 'Paul Bril', 1626, 'Paysage', 'France', null, 'Renaissance', 'Painting', 'Borrowed'),
(22, 'Simone Pignoni', 1698, 'Vierge à l Enfant', 'Egypt', null, 'Renaissance', 'Painting', 'Borrowed'),
(23, 'Paul Bril', 1874, 'Figurine', 'Greece', null, 'Realistic Period', 'Sculpture', 'Borrowed'),
(24, 'Paul Bril', 1929, 'Oiseau', 'Egypt', null, 'Realistic Period', 'Sculpture', 'Borrowed'),
(25, 'Cristoforo Solari', 1550, 'Homme', 'Egypt', null, 'Renaissance', 'Statue', 'Borrowed'),
(26, 'Antonio Leonelli', 1512, 'Roi', 'Italy', null, 'Renaissance', 'Statue', 'Borrowed');


CREATE TABLE IF NOT EXISTS Painting (
	IDNum			integer,
    PaintType		varchar(30),
    DrawnON			varchar(30),
    Style			varchar(30)
);

INSERT INTO Painting
VALUES
(3, 'Oil', 'Canvas', 'Modern'),
(4, 'Oil', 'Paper', 'Cubism'),
(9, 'Oil', 'Paper', 'Abstract'),
(10, 'Water Colour', 'Wood', 'Cubism'),
(11, 'Primer', 'Canvas', 'Cubism'),
(12, 'Primer', 'Wood', 'Abstract'),
(13, 'Water Colour', 'Canvas', 'Cubism'),
(21, 'Primer', 'Canvas', 'Abstract'),
(22, 'Oil', 'Wood', 'Modern');


CREATE TABLE IF NOT EXISTS Sculpture (
	IDNum			integer,
    Material		varchar(30),
    Height			varchar(30),
    Weight			varchar(30),
    Style			varchar(30)
);

INSERT INTO Sculpture
VALUES
(1, 'Gold', '20 cm', '3.3 kg', 'Roman'),
(2, 'Bronze', '15 cm', '2.1 kg', 'Equestrian '),
(14, 'Stone', '17 cm', '2.5 kg', 'Equestrian '),
(15, 'Stone', '9 cm', '1.1 kg', 'Roman'),
(16, 'Bronze', '33 cm', '3.7 kg', 'High Renaissance'),
(23, 'Stone', '7 cm', '0.7 kg', 'High Renaissance'),
(24, 'Gold', '23 cm', '3.4 kg', 'Roman');


CREATE TABLE IF NOT EXISTS Statue (
	IDNum			integer,
    Material		varchar(30),
    Height			varchar(30),
    Weight			varchar(30),
    Style			varchar(30)
);

INSERT INTO Statue
VALUES
(5, 'Marble', '183 cm', '74 kg','Equestrian'),
(6, 'Ceramic', '76 cm', '13 kg','Roman '),
(17, 'Resin', '263 cm', '237 kg','High Renaissance'),
(18, 'Ceramic', '149 cm', '98 kg','High Renaissance'),
(19, 'Resin', '54 cm', '7 kg','Roman'),
(25, 'Marble', '12 cm', '2 kg', 'Equestrian'),
(26, 'Resin', '17 cm', '3 kg', 'High Renaissance');


CREATE TABLE IF NOT EXISTS Other (
	IDNum		integer,
    Type		varchar(30),
    Style		varchar(30)
);

INSERT INTO Other
VALUES
(7, 'Book', 'Religious'),
(8, 'Book', 'Horror');


CREATE TABLE IF NOT EXISTS Permanent (
	IDNum				integer,
    DateAcquired		date,
    PaintingStatus		varchar(30),
    Cost				double
);

INSERT INTO Permanent
VALUES
(1, 20100120, 'On Display', 3124.00),
(2, 20120221, 'Loan', 1200.00),
(3, 20150322, 'Stored', 1765.00),
(4, 20130423, 'Stolen', 2789.00),
(5, 20110524, 'On Display', 2200.00),
(6, 20170625, 'On Display', 975.00),
(7, 20220726, 'On Display', 8750.00),
(8, 20170827, 'Loan', 3172.00),
(9, 20160928, 'Loan', 5900.00),
(10, 20121029, 'Stolen', 6700.00),
(11, 20111130, 'Stored', 535.00),
(12, 20101231, 'Stored', 2450.00),
(13, 20100101, 'Loan', 2790.00),
(14, 20130202, 'On Display', 7500.00),
(15, 20160303, 'Stored', 8720.00),
(16, 20170404, 'On Display', 6310.00),
(17, 20160505, 'On Display', 4300.00),
(18, 20190606, 'Stored', 9730.00),
(19, 20210707, 'Stored', 5250.00),
(20, 20220808, 'On Display', 275.00);


CREATE TABLE IF NOT EXISTS Borrowed (
	IDNum				integer,
    Collection			varchar(30),
    DateBorrowed		date,
    DateReturned		date
);

INSERT INTO Borrowed
VALUES
(21,'Queens, Kings, and Emperrors' , 20130415, 20140415),
(22, 'Major Events in History', 20160517, 20160617),
(23, 'MasterPieces of The Louvre', 20190619, 20210619),
(24, 'Major Events in History', 20220721, 20221021),
(25, 'Queens, Kings, and Emperrors', 20100823, 20110423),
(26, 'Major Events in History', 20070925, 20071005);


CREATE TABLE IF NOT EXISTS Artist (
	Name				varchar(30),
    DateBorn			integer,
    DateDied			integer,
    Country				varchar(30),
    MainStyle			varchar(30),
    Description			varchar(30),
    primary key (Name)
);

INSERT INTO Artist
VALUES
('Benedetto da Rovezzano', 1474, 1552, 'Italy', 'Abstract', null),
('George Gower', 1540, 1596, 'England','Cubism', null),
('Hans Holbein', 1497, 1543, 'Germany', 'Cubism', null),
('Master of Claude', 1510, 1515, 'France', 'Literature', null),
('Lucas Horenbout', 1495, 1544, 'England', 'Portrait', null),
('Antonio Leonelli', 1441, 1525, 'Italy', 'Abstract', null),
('Pablo Picasso', 1881, 1973, 'Spain', 'Abstract', null),
('Georges Braque', 1882, 1963, 'France', 'Modern', null),
('Juan Gris', 1887, 1927, 'Spain', 'Portrait', null),
('Marcos Correa', 1609, 1690, 'Portugal', 'Abstract', null),
('Jean-Baptiste Carpeaux', 1827, 1875, 'France', 'Equestrian', null),
('Cristoforo Stati', 1556, 1619, 'Italy', 'Roman', null),
('Giovanni Caccini', 1556, 1613, 'Italy', 'Roman', null),
('Antonio Canova', 1757, 1822, 'Italy', 'Abstract', null),
('Paul Bril', 1554, 1626, 'Italy', 'Cubism', null),
('Simone Pignoni', 1611, 1698, 'Italy', 'Abstract', null),
('Cristoforo Solari', 1460, 1527, 'Italy', 'Cubism', null);


CREATE TABLE IF NOT EXISTS Collection (
	Name					varchar(30),
    Type					varchar(30),
    Description				varchar(30),
    Address					varchar(50),
    Phone					integer,
    ContactPerson			varchar(30),
    primary key (Name)
);

INSERT INTO Collection
VALUES
('Queens, Kings, and Emperrors', 'Politics', null, '3229 Vineyard Drive, Cleveland', 944-626-2119, 'Lowell Rexana'),
('Major Events in History', 'History', null, '3245 Wetzel Lane, Ellis Township', 282-578-4180, 'Fleurette Charlotte'),
('MasterPieces of The Louvre', 'Miscellaneous', null, '4802 Whitetail Lane, Dallas', 469-342-2170, 'Gyles Ludovic');


CREATE TABLE IF NOT EXISTS Exhibition (
	Name			varchar(30),
    StartDate		date,
    EndDate			date
);

INSERT INTO Exhibition
VALUES
('Vivid Delight', 20130513, 20130520),
('Paper Threads', 20191006, 20191009),
('Context House', 20210102, 20210112),
('Art Simpson', 20220526, 20220601),
('The Art City', 20100226, 20100228);