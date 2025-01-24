# EXPLANATIONS

At the bottom of the footer, we find links to the site’s social media accounts. Upon inspecting the page, it becomes clear that the site to which users are redirected is passed as a parameter in the redirection URL without any validation.

This is a classic case of **open redirection vulnerability** that can lead to **phishing attacks**

⇒ It is technically possible to modify these links to redirect users to malicious sites.
The initial URL (before redirection) appears legitimate because it contains the official domain of the site (e.g., https://site.com/redirect), making it deceptive.

Example:
https://sitedelabanque.com/redirect?site=anything.com

A scammer could send an email to users, asking them to change their password by accessing this URL. By clicking the link, users are redirected to a site that seems legitimate since the base URL is correct. They might then enter their login information and get hacked.

When attempting to modify the HTML in the source code to redirect to another site, such as Wikipedia, a flag is revealed **b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3**

# SOLUTIONS

1. Validate and Whitelist URLs (making sure the URLs are allowed)

2. Sanitize user inputs thoroughly

