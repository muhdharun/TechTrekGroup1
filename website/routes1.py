from flask import Blueprint, Flask, Response, request
from .models import User,Post,LikedPost,PostComment
from . import db
import json
import random

routes1 = Blueprint('routes1', __name__)

@routes1.route('/getAllPosts', methods=['GET'])
def getAllPosts():
    response = None
    try:

        data = {
        "Post_ID": 1,
        "Post_Title": "Relatable",
        "Post_Description": "Walking up and down the aisles for what seems like hours.",
        "Post_image": "https://preview.redd.it/jjvqtw9iapb81.gif?format=mp4&s=e333e78478df813b5b18ecd0905efc8b00ae210c"
    }

        response = Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)

        response = Response(
            response=json.dumps({"message":"cannot get posts"}),
            status=500,
            mimetype="application/json"
        )

    return response

@routes1.route('/createPost', methods=['POST'])
def createPost():
    response = None
    try:
        postId = random.randint(1,1000000)
        post = {"Post_ID": postId, "Post_Title": request.form["title"], "Post_Description": request.form["description"], "Post_Image": request.form["image"]}
        db.session.add(post)
        db.session.commit()

        response = Response(
            response=json.dumps({"message":"post created", "id":f'{postId}'}),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)

        response = Response(
            response=json.dumps({"message":"cannot create post"}),
            status=500,
            mimetype="application/json"
        )

    return response

#get logged in user's posts
@routes1.route('/getPosts', methods=['GET'])
def getPosts():
    return "own posts"