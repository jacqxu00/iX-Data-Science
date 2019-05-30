-- all questions refer to https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

-- 1. Select the first ten records from the OrderDetails table.
SELECT * FROM OrderDetails LIMIT 10;

-- 2. Find the Address for Peter Franken.
SELECT Address FROM Customers WHERE ContactName = "Peter Franken";

-- 3. Find the the costumers who live in spain and whose name begins with 'M'.
SELECT ContactName FROM Customers WHERE Country = "Spain" AND ContactName LIKE "M%";

-- 4. Find the last three costumers from france.
SELECT * FROM Customers WHERE Country = "France" ORDER BY CustomerID DESC LIMIT 3;

-- 5. Find the number of costumers from USA And Germeny combined.
SELECT COUNT(*) FROM Customers WHERE (Country = "USA" OR Country = "Germany");

-- 6. Find the number of for each country.
SELECT Country, COUNT(*) AS Total FROM Customers GROUP BY Country;

-- 7. What is the average quantity in each order detail
SELECT AVG(Quantity) FROM OrderDetails;

-- 8. Who is the customer with the shortest name?
SELECT ContactName FROM Customers ORDER BY LENGTH(ContactName) LIMIT 1;

-- 9. What is the average number of costumers per country?
SELECT (SELECT COUNT(*) FROM Customers) * 1.0 / (SELECT COUNT(DISTINCT Country) FROM Customers);