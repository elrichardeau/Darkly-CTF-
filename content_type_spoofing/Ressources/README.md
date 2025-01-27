# EXPLANATIONS

After doing some research we discover that it is possible to upload scripts instead of images by setting the Content-Type header in the POST request to that of an image type. This tricks the website into expecting a standard image but receiving a script instead.
We try to upload files at http://127.0.0.1:8080/index.php?page=upload.

A simple script, such as a script.py (provided in the directory) is created.

Using Postman, a POST request is made to http://127.0.0.1:8080/index.php?page=upload.

In the body of the request, two key-value pairs are created:

1. uploaded: Since in the HTML the "Choose File" button is associated with <input name="uploaded" type="file">, the file is submitted under this name. The content type is set to image/jpeg. This simulates adding a file.

2. Upload: Corresponds to the name of the "upload" button in the HTML, which is used to trigger the file upload action.

When these manipulated headers are sent, the server is tricked into processing the file as an image, but it’s actually a script. We get the flag:
**46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8**

# SOLUTIONS

1. Check files permissions and do not allow executable files or scripts

2. Rename all files with non-executable extensions (.jpg, .jpeg...)

3. Do not rely only on content-type : also chech file extension (and use a whitelist of allowed extensions)