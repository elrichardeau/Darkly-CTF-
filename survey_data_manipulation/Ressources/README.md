# EXPLANATIONS

At the URL http://127.0.0.1:8080/index.php?page=feedback, in the surveys, we can only enter values from 0 to 10. By inspecting the page we try to directly modify the HTML to enter higher values (for example 10 000) and... it works! We get the flag: **03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa**

This allows us to manipulate the statistics as we wish.

# SOLUTIONS

1. Always validate inputs on the server (check if the values are between 0 and 10 in this example)

2. Authorize one feedback per IP or logged in account (or use CAPTCHA to prevent bots from repeatedly submitting responses)