# EXPLANATIONS

Upon checking the session cookies, we notice that one of them is called "i_am_admin" which seems intriguing.
Its associated value is 68934a3e9455fa72420237eb05902327

We search for this value on Internet and discover the concept of **MD5**, a protocol for encrypting hashes.

We go to a website that allows decrypting and encrypting hashses: <https://md5decrypt.net/>

After decrypting the value we get the "translation" of the cookie: "false".
Since the cookie is named "i_am_admin" and its value is "false", we deduce that we need to encrypt "true". We replace the value in the cookie and the flag appears:
**df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3**

# SOLUTIONS

Avoid trusting client-side cookies, always validate sensitive data (ex: is_admin) on the server side and store it via a unique session ID rather than storing it in a cookie.
Use stronger hashing algorithms, sign and validate cookies (a signed cookie ensures that the data has not been modified by the client)