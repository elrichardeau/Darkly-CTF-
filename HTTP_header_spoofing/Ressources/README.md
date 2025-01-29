# EXPLANATIONS

Upon inspecting the homepage, we discover a hidden link in the footer that is not apparent on the site: <a href="?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"></a>

It directs us to a page with music. Upon inspecting this page, we find a text containing the phrase 'You must come from: “https://www.nsa.gov/”' and another hint 'Let's use this browser: “ft_bornToSec”. It will help you a lot.'

This likely concerns HTTP headers. We use Postman to modify the two parameters provided by the page: the user-agent (ft_borntoSec), which is the name of the browser (browser name and version), and the referer (nsa.gov), which is the URL of the page from which the request was made (indicating to the server from which page or site the user is coming).

Example of user-agent: User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36

Example of referer: Referer: https://www.google.com/search?q=example"

Bingo, it worked ! We get the flag 
**f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188**

This vulnerability allows attackers to manipulate the User-Agent and Referer headers in HTTP requests, potentially bypassing security mechanisms that rely on those headers for authentication or access control.

# SOLUTIONS

1. Rely on strong authentication mechanisms (session tokens, API keys, OAuth) rather than HTTP headers

2. Use a WAF (web application firewall) since they can inspect and block incoming requests that contain malicious or malformed HTTP headers
