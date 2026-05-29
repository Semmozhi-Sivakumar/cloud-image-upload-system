
from flask import Flask, request, render_template
import boto3

app = Flask(__name__)

s3 = boto3.client(
    's3',
    aws_access_key_id='your_access_key',
    aws_secret_access_key='your_secret_key',
    region_name='ap-south-1'
)

BUCKET_NAME = 'blue-image-app'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']

    if file:

        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.filename,
            ExtraArgs={
                "ContentType": file.content_type,
                "ACL": "public-read"
            }
        )

        url = f"https://{BUCKET_NAME}.s3.ap-south-1.amazonaws.com/{file.filename}"

        return render_template(
            'index.html',
            image_url=url
        )

    return "No file uploaded"

if __name__ == '__main__':
    app.run(debug=True)