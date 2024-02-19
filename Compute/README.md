# Flask App with Gunicorn

This is a Flask app that can be run using Gunicorn. It exposes three endpoints for uploading, downloading and deleting images from a bucket in OCI Object Storage.

## Table of Contents

- [Flask App with Gunicorn](#flask-app-with-gunicorn)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Clone the repository](#clone-the-repository)
    - [Create a Python virtual environment (venv)](#create-a-python-virtual-environment-venv)
    - [Activate the virtual environment](#activate-the-virtual-environment)
    - [Install the requirements](#install-the-requirements)
    - [Add your OCI Bucket name](#in-env-add-your-oci-bucket-name)
    - [Run the app in debug mode](#run-the-app-in-debug-mode)
  - [Test](#test)
    - [Upload a picture](#upload-a-picture)
    - [Download a picture](#download-a-picture)
    - [Delete a picture](#delete-a-picture)
  - [Deploy](#deploy)
    - [Change app.py to run in production mode](#change-app-py-to-run-in-production-mode)
    - [Start a multi-process gunicorn server](#start-a-multi-process-gunicorn-server)

## Prerequisites

- Python 3.x
- Flask
- Gunicorn
- OCI Python SDK
- OCI CLI

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Create a Python virtual environment (venv)

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment

    ```bash
    source venv/bin/activate
    ```

4. Install the requirements

    ```bash
    pip install -r requirements.txt
    ```

5. In `.env`, add your OCI Bucket name

6. Run the app in debug mode

    ```bash
    python3 app.py
    ```

## Test

### Upload a picture

```bash
curl -X POST -F "file=@/Users/${whoami}/Downloads/my_picture.jpg" http://localhost:5000/pictures/avatar.jpg
```

### Download a picture

```bash
curl -X GET http://localhost:5000/pictures/avatar.jpg -o downloaded_file.jpg
```

### Delete a picture

```bash
curl -X DELETE http://localhost:5000/pictures/avatar.jpg
```

## Deploy

1. Change `app.py` to run in production mode:

    ```bash
    if __name__ == '__main__':
        app.run(debug=False)
    ```

2. Start a multi-process gunicorn server:

    ```bash
    gunicorn -w 4 app:app
    ```