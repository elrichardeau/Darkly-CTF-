# EXPLANATIONS

From the login page, we attempt to log in as an admin. To do this, we use a list of 20 common passwords found on Wikipedia (e.g., 123, qwerty, letmein, password123...), and a simple bash script like the one provided (login.sh) which uses these passwords and attempts to simulate a login. One of them works: shadow.
We get the flag : **b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2**


# SOLUTIONS

Enforce strong password policies of course, block login attempts from this IP address after a certain number of failed attempts (ex: 3), enable 2 Factor-Authentication 
