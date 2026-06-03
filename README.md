Task 2.Write sql queries that fetch the following data: 
-> sales_per_day

SELECT DATE(sales.created_at) AS sale_date, SUM(sales.quantity * products.selling_price) AS sales_per_day FROM sales JOIN products ON sales.pid = products.id GROUP BY DATE(created_at) 
ORDER BY sale_date; 

-> profit_per_day 

SELECT DATE(sales.created_at) AS sale_date, SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit_per_day FROM sales JOIN products ON sales.pid = products.id GROUP BY DATE(created_at) ORDER BY sale_date;

-> sales_per_product 

SELECT name, SUM(sales.quantity) AS sales_per_product FROM sales
JOIN products ON sales.pid = products.id GROUP BY name;

-> profit_per_product

SELECT name, SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit_per_product FROM sales JOIN products ON sales.pid = products.id GROUP BY name;

class: Horse
State: colour,breed,gender
behaviour: sleep,gallop,feed

class: Student
state: gender,age,class/form
behaviour: read,write

class: Car
State:model,colour, make
Behavior: reverse,drive,maneuver,stop,navigation
