# EXPLANATIONS

Click on 'login' then on 'forgot password' to see a 'submit' field appear with nothing else on the page, which is strange since we should usually be able to enter an email to receive the new password.

Upon inspecting the page to search for a potential 'email' field, we notice there is a field in the body, already filled with an email: the email of the admin who will receive the new passwords requests.

We try to modify the email in the HTML and by refreshing the page, surprise, we get the flag : **1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0**

Being able to access the email is a common source of vulnerabilities, including: 

1. **Email spoofing**: if an attacker modifies the email field, they can redirect password reset instructions and sensitive data to their own email address.

2. **Email bombing**: an attacker can write a script to overload the email account. The admin's inbox can be flooded with password reset requests. This could overwhelm the server.


# SOLUTIONS

1. Avoid exposing sensitive data, such as this admin address (use backend processes to handle sensitive information, not frontend processes)

2. When the user asks for a new password, he should be able to enter his own email address. The server should verify if this address exists and if it is valid, generate a secure token and send a reset link to this email.
