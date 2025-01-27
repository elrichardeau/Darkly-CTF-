# EXPLANATIONS

By researching common vulnerabilities online, we discover the existence of **directory traversal vulnerabilities**: security flaws that allow attackers to traverse the file system hierarchy beyond authorized limits and access sensitive files.

For example, if the URL includes a "page" parameter:

*http://example.com/index.php?page=contact*

We can replace the contact page with other paths, like ../../, to attempt to move up the directory hierarchy. This can be used to try to access files such as /etc/passwd or .env files.

By trying ../, we quickly realize we are on the right track because the site returns pop-ups with jokes like "nope…", "that’s better…", and "wtf?!". We test many combinations and are guided to add more and more ../../ in the path. We also test different filenames (like etc/passwd, etc/shadow...)

When trying this combination : *http://127.0.0.1:8080/index.php?page=../../../../../../../etc/shadow*

We get the flag : 
**b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0**

# SOLUTIONS 

Sanitize user input (reject or normalize input containing potentially dangerous sequences like ../ or /, with the function basename for example), use a whitelist of allowed pages, block access to sensitive system files (/etc/passwd, /etc/shadow...), use a WAF (web application firewall) since they can detect and block malicious URL patterns or file access attempts that indicate a directory traversal attack.