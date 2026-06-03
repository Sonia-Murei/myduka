Task 2.Write sql queries that fetch the following data: 
-> sales_per_day

SELECT DATE(created_at) AS sale_date, SUM(Quantity) AS sales_per_day FROM sales GROUP BY DATE(created_at) ORDER BY sale_date; 

-> profit_per_day 

SELECT DATE(sales.created_at) AS sale_date, SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit_per_day FROM sales JOIN products ON sales.pid = products.id GROUP BY DATE(created_at) ORDER BY sale_date;

-> sales_per_product 

SELECT name, SUM(sales.quantity) AS sales_per_product FROM sales
JOIN products ON sales.pid = products.id GROUP BY name;

-> profit_per_product

SELECT name, SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit_per_product FROM sales JOIN products ON sales.pid = products.id GROUP BY name;
