from app import app
from flask import jsonify, redirect, request, url_for
from tinydb import TinyDB
import json


from .modules import Test, Note, db
from config import TINYDBPATH

BASE_API = "/api/v1/"



############# ERROR HANDLING
#standard flask error message is not pretty, overwriting it
@app.errorhandler(405)
def method_not_allowed(err):
    return jsonify({"msg": "method not allowed for this route"})

@app.errorhandler(404)
def path_not_found(err):
    return jsonify({"msg": "path does not exist"})




############# API ROUTES
# base case without specific route provided => redirect
@app.route("/", methods=["GET"])
def reroute():
    return redirect(url_for("index"))

@app.route(BASE_API, methods=["GET"])
def index():

    d_load = {"msg": "This is a test API for the EF interview coding challenge"}
    return jsonify(d_load)



# CREATE NOTE
@app.route(BASE_API + "note/create/", methods=["POST"])
def create():

    data = json.loads(request.data)
    title = data.get("title", None)
    content = data.get("content", None)
    if not content: return jsonify({"msg": "no content provided"})
    if not title: title = "New Note"
    
    note = Note()
    note.content = content
    note.title = title
    id = note.create(content=content, title=title)
    return jsonify({"msg": "success", "description": "note created", "note_id": id})

# GET NOTE
@app.route(BASE_API + "note/get/", methods=["GET"])
def get():
    
    data = json.loads(request.data)
    id = data.get("id", None)
    note = Note(id)
    return note.get_note()

# LIST NOTES
@app.route(BASE_API + "note/list/", methods=["GET"])
def list():
    return jsonify(db.all())

# DELETE NOTE
@app.route(BASE_API + "note/delete/", methods=["DELETE"])
def delete():
    data = json.loads(request.data)
    id = data.get("id", None)
    note = Note(id)
    return note.delete_note()

# UPDATE NOTE
@app.route(BASE_API + "note/edit/", methods=["POST"])
def update_note():
    data = json.loads(request.data)
    id = data.get("id", None)
    content = data.get("content", None)
    title = data.get("title", None)

    note = Note(id)
    return note.edit_note(title=title, content=content)


