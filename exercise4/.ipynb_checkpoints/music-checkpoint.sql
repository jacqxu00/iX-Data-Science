-- ====================================================================================================================
-- SQL TUTORIAL: MUSIC
-- ====================================================================================================================

-- COLUMN TYPES -------------------------------------------------------------------------------------------------------

-- Not all column types are available in all database implementations. Below is a subset of the most important types.

-- Text
-- ====
--
-- CHAR          Fixed length string.
-- VARCHAR       Variable length string.

-- Numeric
-- =======
--
-- TINYINT       -128 to 127.
-- SMALLINT      -32768 to 32767.
-- MEDIUMINT     -8388608 to 8388607.
-- INT           -2147483648 to 2147483647.
-- BIGINT        -9223372036854775808 to 9223372036854775807.
-- DECIMAL       Stored as a string, allowing for a fixed decimal point.
-- FLOAT         Single precision floating point.
-- DOUBLE        Double precision floating point.
--
-- There are also UNSIGNED versions of the INT types.

-- Date
-- ====
--
-- DATE()        YYYY-MM-DD.
-- DATETIME()    YYYY-MM-DD hh:mm:ss
-- TIMESTAMP()   Number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).
-- TIME()        hh:mm:ss

-- USER ---------------------------------------------------------------------------------------------------------------
SHOW PRIVILEGES;

-- DATABASE -----------------------------------------------------------------------------------------------------------

SHOW DATABASES;

-- CREATE DATABASE ----------------------------------------------------------------------------------------------------

-- Create a new database.
--
-- If there are multiple users on the same server then each will have to choose a unique name for their database.
--
CREATE DATABASE music;
--
-- To make the database name unique, append your username. For example, 'music_datawookie'.

-- Select the newly created database.
--
USE music;


-- CREATE TABLE -------------------------------------------------------------------------------------------------------

-- Create a table in the database.
--
CREATE TABLE musician (
    name                        VARCHAR(64) NOT NULL,
    gender                      CHAR(1),
    birth                       DATE,
    band_name                   VARCHAR(64),
    band_type                   VARCHAR(32)
);

-- Notes:
--
-- * NOT NULL is a constraint indicating that the field cannot be left empty.

-- Take a look at the table structure.
--
EXPLAIN musician;
--
SHOW CREATE TABLE musician;

-- INSERT -------------------------------------------------------------------------------------------------------------

-- Inserting a subset of fields.
--
INSERT INTO musician (name, band_name) VALUES ('John Lennon', 'The Beatles');

-- Inserting all fields.
--
INSERT INTO musician VALUES ('Paul McCartney', 'M', '1942-06-18', 'The Beatles', 'Pop');

SELECT * FROM musician;

-- Inserting multiple records.
--
INSERT INTO
			musician (name, band_name)
VALUES
			('Ringo Starr', 'The Beatles'),
			('George Harrison', 'The Beatles'),
			('Pete Best', 'The Beatles');

-- Add in a few solo musicians.
--
INSERT INTO musician (name) VALUES ('Neil Young'), ('Bob Dylan'), ('Carole King'), ('Joni Mitchell');

-- Test the NOT NULL constraint. This statement will FAIL.
--
INSERT INTO musician (name, gender, band_name) VALUES (NULL, 'M', 'The Troggs');

-- Notes:
--
-- * There is nothing stopping you from inserting duplicate records.

-- SELECT -------------------------------------------------------------------------------------------------------------

-- Retrieve all fields from all records.
--
SELECT * FROM musician;

-- Retrieve a selection of fields from all records.
--
SELECT name, gender FROM musician;

-- A WHERE clause applies a filter, selecting only those records which satisfy a logical predicate.
--
SELECT * FROM musician WHERE birth = '1942-06-18';
--
SELECT * FROM musician WHERE birth IS NOT NULL;
--
SELECT * FROM musician WHERE name LIKE 'J%';

-- Notes:
--
-- * Predicates can be combined with AND and OR.
-- * Operations for predicates:
--
--     - arithmetic operations
--     - relational operations (=, <>, >, <, >=, <=, BETWEEN)
--     - IS NULL and IS NOT NULL
--     - LIKE
--     - IN

-- Exercises:
--
-- * Select musicians whose name begins with either 'J' or 'P'.
-- * Select musicians whose name begins with either 'J' or 'P' and who are members of The Beatles.

-- UPDATE -------------------------------------------------------------------------------------------------------------

-- We need to make MySQL a little more permissive with UPDATE.
--
SET SQL_SAFE_UPDATES = 0;

-- Change field in all records.

--
UPDATE musician SET gender = 'M';

-- Change field in records selected by predicate.
--
UPDATE
			musician
SET
			gender = 'F'
WHERE
			name IN ('Carole King', 'Joni Mitchell');

-- Change multiple fields simultaneously.
--
UPDATE
			musician
SET
			birth = '1940-10-09',
			band_type = 'Pop'
WHERE
			name = 'John Lennon';

-- Exercises:
--
-- * Populate all fields for the remaining musicians.

-- DELETE -------------------------------------------------------------------------------------------------------------

DELETE FROM musician WHERE name = 'Pete Best';
--
-- Only *real* members of The Beatles!

-- ALTER --------------------------------------------------------------------------------------------------------------

-- Add a column to an existing table.
--
ALTER TABLE musician ADD COLUMN death DATE;

-- Notes:
--
-- * To remove a column use DROP COLUMN.
-- * To change the data type for a column use ALTER COLUMN or MODIFY COLUMN.

-- Exercises:
--
-- * Update the death field for the deceased musicians.

-- NORMALISATION ------------------------------------------------------------------------------------------------------

-- There are a variety of problems with the table we've been working with, foremost is the fact that information is
-- duplicated between records. What happens if we want to change the band name?

-- Normalisation is the process of organising tables and columns to reduce redundancy. Simply stated, normalisation
-- breaks down data into a set of linked tables.

-- PRIMARY KEY --------------------------------------------------------------------------------------------------------

-- Create a table for bands.
--
-- The id column is a PRIMARY KEY, which is used to uniquely identify each record in the table.
--
CREATE TABLE band (
    id                          INT NOT NULL AUTO_INCREMENT,
    name                        VARCHAR(64) NOT NULL,
    type                        VARCHAR(32),
    PRIMARY KEY (id)
);

-- Add a primary key to the musician table.
--
ALTER TABLE musician ADD COLUMN id INT PRIMARY KEY NOT NULL AUTO_INCREMENT FIRST;

-- Insert a record for The Beatles.
--
INSERT INTO band (name, type) VALUES ('The Beatles', 'Pop');

-- Exercises:
--
-- * Add a band_id column (type INT DEFAULT NULL) to the musician table.
-- * Update the band_id values so that they point to the correct records in the band table. We'll do this manually at
--   the moment but soon we'll see a way to do it with a query.
-- * Drop the band_name and band_type columns from the musician table.

ALTER TABLE musician DROP COLUMN band_type DROP COLUMN band_name;


ALTER TABLE musician ADD COLUMN band_id INT DEFAULT NULL;

UPDATE musician SET band_id = 1 WHERE id = 1;

-- FOREIGN KEY CONSTRAINTS --------------------------------------------------------------------------------------------

-- The link between the musician and band tables is currently just a formality. We need to add a foreign key
-- constraint to enforce this link.
--
ALTER TABLE musician
ADD FOREIGN KEY (band_id) REFERENCES band(id);

-- Exercises:
--
-- * Try to remove The Beatles from the band table. What happened?

CREATE TABLE album (
    id                          INT NOT NULL AUTO_INCREMENT,
    name                        VARCHAR(64) NOT NULL,
    released                    DATE,
    band_id                     INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (band_id) REFERENCES band(id)
);
CREATE TABLE song (
    id                          INT NOT NULL AUTO_INCREMENT,
    name                        VARCHAR(64) NOT NULL,
    track                       TINYINT UNSIGNED,
    album_id                    INT,
    PRIMARY KEY (id),
    FOREIGN KEY (album_id) REFERENCES album(id)
);

-- Exercises:
--
-- * Create records for the 'Rubber Soul' and 'Abbey Road' albums.
      
-- * Create records for the tracks 'Nowhere Man' and 'Drive My Car' on the 'Rubber Soul' album.
-- * [EXTRA CREDIT] Add a new band with associated musicians, an album and a few songs. Everybody does this on a
--   single database.

-- RELATIONSHIPS ------------------------------------------------------------------------------------------------------

-- ONE-TO-ONE
--
-- It's possible to establish a one-to-one relationship but this is rather a niche requirement, so we are not going to
-- look at it in detail.

-- ONE-TO-MANY
--
-- A one-to-many relationship is catered for via primary and foreign keys.
--
-- For example, one band is mapped to many musicians.

-- MANY-TO-MANY
--
-- A many-to-many relationship is created using a junction table.
--
-- For example, we might create an instrument table. An artist might play multiple instruments and an instrument might
-- be played by multiple artists.

CREATE TABLE instrument (
    id                          INT NOT NULL AUTO_INCREMENT,
    name                        VARCHAR(64) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE instrument_musician (
    id                          INT NOT NULL AUTO_INCREMENT,
    musician_id                 INT NOT NULL,
    instrument_id               INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (musician_id) REFERENCES musician(id),
    FOREIGN KEY (instrument_id) REFERENCES instrument(id)
);

INSERT INTO instrument (name) VALUES ('vocals'), ('guitar'), ('keyboard'), ('harmonica'), ('drums'), ('sitar');

INSERT INTO instrument_musician (musician_id, instrument_id)
VALUES (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (3, 1), (3, 5), (4, 1), (4, 2), (4, 6);

-- JOINS --------------------------------------------------------------------------------------------------------------

-- INNER JOIN
--
-- An inner join effectively considers the intersection of two tables.
--
-- +----------------------+          
-- |                      |          
-- |                      |          
-- |                      |          
-- |                      |          
-- |         +----------------------+
-- |         |............|         |
-- |         |............|         |
-- |         |............|         |
-- |         |............|         |
-- |         |............|         |
-- |         |............|         |
-- +---------|------------+         |
--           |                      |
--           |                      |
--           |                      |
--           |                      |
--           +----------------------+
--
SELECT *
FROM
        musician
INNER JOIN
        band
ON
        musician.band_id = band.id;

-- Notes:
--
-- * The result only contains records for which there is a match between the tables.

-- Exercises:
--
-- * Select the names of the members of The Beatles.

-- OUTER JOINS
--
-- An outer join effectively considers the (one sided) union of two tables.
--
-- +----------------------+          
-- |......................|          
-- |......................|          
-- |......................|          
-- |......................|          
-- |.........+----------------------+
-- |.........|............|         |
-- |.........|............|         |
-- |.........|............|         |
-- |.........|............|         |
-- |.........|............|         |
-- |.........|............|         |
-- +---------|------------+         |
--           |                      |
--           |                      |
--           |                      |
--           |                      |
--           +----------------------+
--
SELECT *
FROM
        musician
LEFT JOIN
        band
ON
        musician.band_id = band.id;

-- Notes:
--
-- * The result contains all records from musician regardless of whether there is a match in band.
-- * There is also a RIGHT JOIN which does the same thing but for tables listed in opposite order.

-- Exercises:
--
-- * Select the only the musician and band names. Relabel the result columns accordingly.

-- Joining via a junction table.
--
SELECT A.name AS musician, C.name AS instrument
FROM
        musician A
INNER JOIN
        instrument_musician B
ON
        A.id = B.musician_id
INNER JOIN
        instrument C
ON
        C.id = B.instrument_id
ORDER BY
        instrument;

-- CREATING TABLES WITH QUERIES ---------------------------------------------------------------------------------------

-- We can also create and populate a table using SELECT.
--
CREATE TABLE solo AS (
    SELECT name FROM musician WHERE band_id IS NULL
);

-- Temporary tables can be very useful for decomposing complicated queries. However they only last for the duration of
-- the session.
--
-- The following two statements must be executed in the same transaction under phpMyAdmin because it closes the
-- database connection after each transaction.
--
CREATE TEMPORARY TABLE IF NOT EXISTS female_musicians
AS (
    SELECT name FROM musician WHERE gender = 'F'
);
--
SELECT * FROM female_musicians;


-- DROP TABLE ---------------------------------------------------------------------------------------------------------

-- When we no longer need a table it can be dropped.
--
-- [!!!] WARNING: This is irreversible!
--
DROP TABLE solo;
--
-- Alternatively, if you're not sure whether a table exists...
--
DROP TABLE IF EXISTS solo;

-- DROP DATABASE ------------------------------------------------------------------------------------------------------

-- If we no longer need the database then we can drop it too.
--
-- [!!!] WARNING: This is irreversible!
--
DROP DATABASE music;

-- ====================================================================================================================
--                                                                                                            SOLUTIONS
-- ====================================================================================================================

-- UPDATE -------------------------------------------------------------------------------------------------------------

UPDATE musician SET band_type = "Pop" WHERE band_name = "The Beatles";
UPDATE musician SET birth = "1940-07-07" WHERE NAME LIKE "Ringo%";
UPDATE musician SET birth = "1943-02-25" WHERE NAME LIKE "George%";

-- ALTER --------------------------------------------------------------------------------------------------------------

UPDATE musician SET death = "1980-12-08" WHERE NAME LIKE "John%";
UPDATE musician SET death = "2001-11-29" WHERE NAME LIKE "George%";

-- PRIMARY KEY --------------------------------------------------------------------------------------------------------

ALTER TABLE musician ADD COLUMN band_id INT DEFAULT NULL;

UPDATE musician SET band_id = 1 WHERE band_name = "The Beatles";

ALTER TABLE musician DROP COLUMN band_name;
ALTER TABLE musician DROP COLUMN band_type;

-- FOREIGN KEY CONSTRAINTS --------------------------------------------------------------------------------------------

INSERT INTO album (name, band_id) VALUES ('Rubber Soul', 1), ('Abbey Road', 1);

INSERT INTO song (name, album_id) VALUES ('Nowhere Man', 1), ('Drive My Car', 1);

-- RELATIONSHIPS ------------------------------------------------------------------------------------------------------

-- JOINS --------------------------------------------------------------------------------------------------------------

SELECT musician.name AS musician, gender, birth, death, band.name AS band, type
FROM
        musician
INNER JOIN
        band
ON
        musician.band_id = band.id;


-- DROP TABLE ---------------------------------------------------------------------------------------------------------
DROP TABLE music.musician;

-- DROP DATABASE ------------------------------------------------------------------------------------------------------
DROP DATABASE music;
