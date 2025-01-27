# EXPLANATIONS

We discover the concept of **SQL Injection vulnerabilities.**
Usually, when a user submits a request, the web application queries the database to construct an appropriate response. SQL is the language used to query a database.

An SQL injection (SQLi) is a type of attack in which an attacker inserts a SQL query into regular input fields or forms (for example, a username, password, etc.). This SQL instruction is then passed to the underlying database. If the site is not properly protected, the attacker can directly query the database.
For example, one could input queries into a web app without proper input validation and gain access to client files, sensitive financial information, etc.

On the 'search member' page http://127.0.0.1:8080/index.php?page=member, we try making random queries and receive an error message that indicates that SQL queries can be made. 
To exploit the database, we need to determine its structure, particularly the number of columns. Using the 'ORDER BY' statement, we discover that there are 2 columns in the table.

We try to get more data, particularly the name of the table associated with the search field. We enter:
1 UNION ALL SELECT 1, table_name FROM information_schema.tables WHERE table_schema = database();
and we obtain the name of the table: users.

We try several queries to explore this table, but encounter errors. We assume that the web app checks the input of queries and has blocked the term 'users' because it is too sensitive. A technique to bypass this block is to convert the database name to hexadecimal. We use MD5 (<https://md5decrypt.net/>) for this and try:
1 UNION ALL SELECT 1, column_name FROM information_schema.columns WHERE table_name = 0x7573657273;
Success, it works!! We obtain the column names: user_id, first_name, last_name, town, country, planet, comment, and countersign.

We then enter the command 1 UNION ALL SELECT 1, name_of_the_column FROM users; with each column name we found, and follow the instructions that are given, which involve decrypting the provided password: 5ff9d0165b4f92b14994e5c685cdce28 (with <https://md5decrypt.net/> again) and then running the SH256 command on it. This allows us to obtain the flag :
**10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5**

# SOLUTIONS

1. Use prepared statements : they are placeholders for variables in the SQL query. They ensure that user input is treated as data and not executable code.

2. Sanitize and validate user input

3. Use a WAF (web applicatio firewall)