# cloud-image-upload-system
Image upload and storage system built using Flask, AWS S3, and boto3.
--------------------------------------------------------------------
1. Created a Flask web application to build the backend server and handle image uploads from users through a web browser.

2. Designed the frontend using HTML and CSS with separate templates and static folders for a professional user interface.

3. Created an AWS S3 bucket to store uploaded images in cloud storage instead of saving them locally.

4. Used AWS IAM to create a user with S3 permissions and generated Access Key and Secret Key for secure AWS access.

5. Integrated Python with AWS using boto3, which acts as a bridge between the Flask application and AWS S3 services.

6. Used Flask routes such as `/` and `/upload` to receive image files and process upload requests.

7. Uploaded images to the S3 bucket using `upload_fileobj()` function from boto3.

8. Added `ContentType` metadata while uploading so browsers recognize the file as an image and display it properly.

9. Configured S3 object permissions using ACL and public access settings to make uploaded images accessible through URLs.

10. Generated public S3 URLs dynamically and displayed uploaded images directly in the browser after successful upload.

11. Learned important cloud concepts such as S3 storage, IAM security, ACL permissions, public URLs, metadata handling, Flask backend development, and AWS integration.

12. Debugged and fixed real-world issues including invalid AWS keys, virtual environment problems, Flask installation errors, permission issues, and image download/display behavior.
