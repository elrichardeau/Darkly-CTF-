# EXPLANATIONS

While researching common security vulnerabilities, we came across the existence of the robots.txt file, which is publicly accessible at http://any_website.com/robots.txt.

This file tells search engine bots which URLs they are allowed to access on the site. It is mainly used to prevent overloading the site with requests and provides instructions on which parts of the site bots can or cannot crawl (for example to protect sensitive data).

Sometimes, developers use the Disallow rule to prevent bots from exploring certain directories, but in doing so, they reveal the existence of these directories to anyone who accesses the file.

In this case, we found a /whatever folder containing a file with a root password: root:437394baff5aa33daa618be47b75cb49.

Recognizing the same format as the previous vulnerability involving the MD5 hashing algorithm, we decrypted it and obtained the password: qwerty123@ at <https://md5decrypt.net/>

But where could it be used? It didn’t work with the standard admin login page as it did with the previous password, and there’s no dedicated admin login page available.

After searching online, we discovered a tool called dirb, which can find hidden objects or pages on a website. Running the command dirb http://127.0.0.1:8080 -o dirb.log, we identified two hidden objects: the well-known robots.txt file and the /admin/ page.

We logged in to /admin/ using the username root and the password we found, successfully obtaining the flag:

**d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff**

# SOLUTIONS

1. Do not rely on robots.txt to protect sensitive data

2. Use proper authentication for sensitive directories (/admin should not be accessible to anyone)

3. User .htaccess (server configuration files) to restrict access to specific directories, regardless of what is in robots.txt

4. Use tags within the HTML of the page : the "noindex" tag prevents search engines from indexing the page (<meta name="robots" content="noindex">) while keeping it accessible to authorized users
