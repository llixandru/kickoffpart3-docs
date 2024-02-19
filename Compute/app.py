from flask import Flask, request, Response
from dotenv import load_dotenv
import oci
import os

load_dotenv()

app = Flask(__name__)

config = oci.config.from_file()
object_storage = oci.object_storage.ObjectStorageClient(config)
namespace = object_storage.get_namespace().data
bucket_name = os.getenv("BUCKET_NAME")

@app.route('/<userId>/<filename>.jpg', methods=['POST'])
def upload(userId, filename):
    file = request.files['file']
    object_name = f'{userId}/{filename}.jpg'
    object_storage.put_object(namespace, bucket_name, object_name, file)
    return '', 201

@app.route('/<userId>/<filename>.jpg', methods=['GET'])
def download(userId, filename):
    object_name = f'{userId}/{filename}.jpg'
    get_obj = object_storage.get_object(namespace, bucket_name, object_name)
    return Response(get_obj.data.raw.stream(1024 * 1024, decode_content=False),
                    mimetype=get_obj.headers['content-type'],
                    direct_passthrough=True)

@app.route('/<userId>/<filename>.jpg', methods=['DELETE'])
def delete(userId, filename):
    object_name = f'{userId}/{filename}.jpg'
    object_storage.delete_object(namespace, bucket_name, object_name)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)