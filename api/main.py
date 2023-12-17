""" Main application """
import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import mongo_client

gallery = mongo_client.gallery
images_collection = gallery.images

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
    raise EnvironmentError(
        "Please create the .env.local file with the UNSPLASH_KEY in it."
    )

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = DEBUG


@app.route("/new-image/")
def new_image():
    """New image API"""
    word = request.args.get("query")
    headers = {"Authorization": "Client-ID " + UNSPLASH_KEY, "Accept-Version": "v1"}
    params = {"query": word}

    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    data = response.json()

    return data


@app.route("/images", methods=["GET", "POST"])
def images():
    """Image-handling API"""
    if request.method == "GET":
        # Read images from the database
        images = images_collection.find({})
        return jsonify([img for img in images])
    elif request.method == "POST":
        # Save image in the database
        image = request.get_json()
        image["_id"] = image.get("id")
        result = images_collection.insert_one(image)
        inserted_id = result.inserted_id
        return {"inserted_id": inserted_id}
    else:
        # Invalid operation
        raise EnvironmentError("Invalid operation")


@app.route("/images/<image_id>", methods=["DELETE"])
def image(image_id):
    if request.method == "DELETE":
        # Delete image from the database
        result = images_collection.delete_one({"_id": image_id})
        if not result:
            return {"error": "Image was not deleted"}, 500
        if result and not result.deleted_count:
            return {"error": "Image not found"}, 404
        return {"deleted_id": image_id}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
