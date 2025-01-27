# EXPLANATIONS

Through research, we discover the concept of **Cross-Site Scripting** (XSS) attack. It is a vulnerability in websites that allows injecting content into a page (via scripts), causing actions on the browsers that visit the page.

For example, here the user can leave feedback at this URL: http://127.0.0.1:8080/index.php?page=feedback. We can attempt to inject malicious JavaScript or HTML code. This code would then be executed in the browser of anyone who visits or interacts with the page. The script could steal cookies, session tokens, sensitive data, or redirect the user to a malicious site. If we inject the script and it is stored in a database (for example, to be displayed later, like in a comment section), it will be displayed and executed every time another user views the page.

Upon inspecting the page, we notice that aside from a max_length attribute, there is no protection on the feedback submitted.

I try inserting a script <script>alert('Hello, everyone!')</script> into the feedback. This doesn't work, so there may be some basic sanitization that removes suspicious tags. I try different combinations like "this is a script" and then "script", and finally, I obtain the flag.

**0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e**

# SOLUTIONS

1. Valide and sanitize input (stripping out potentially dangerous characters or have a whitelist of allowed characters and tags)

2. Using a WAF (web application firewall) as they can help detect and block common XSS attacks

3. When rendering data like user input in HTML, encode it properly so that's is always interpreted as data and not executable code (example: replace < with &lt)
