# EXPLANATIONS

When browsing the site, we notice that one of the images redirects us to another page that displays the name of the loaded file.
Upon inspecting the page we can see this line of code : <a href="?page=media&src=nsa"><img src="images/nsa_prism.jpg" alt=""></a>

There is a clickable link. The href attribute contains a query string ?page=media&src=nsa. When a user clicks this link the browser will load the page.
We can try to exploit the "src" variable, for example to make the browser execute a script when clicking on the image.

We try to modify 'nsa' with a script <script>alert(1);</script> but it doesn't work because the browser treats it as plain text part of the URL (= a path) and not as executable code.

I need to encode our script in base64, which doesn’t resemble typical JS or HTML and can be executed by the browser after being decoded. Writing a script in base64 helps bypass certain protections the site may use to prevent executing malicious JS. The characters generated are not seen as executable code and bypass validations that block direct JS injections.

For example, trying to write the following script <script>alert(1);</script> doesn’t work.

By encoding it in base64, we get: data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=

Interacting with the image after modifying the page's code gives us the flag:

**928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d**

It is called "reflected" because the malicious code is directly reflected by the server in its response. The malicious input is not stored, in contrast to stored XSS. The code is executed immediately when the victim accesses the URL and does not persist once the response is sent.

# SOLUTIONS

1. Sanitize user input

2. Server-side validation