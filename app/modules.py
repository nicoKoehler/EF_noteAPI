
import json
from logging.handlers import QueueListener
from tabnanny import check
from urllib import response
from flask import jsonify
from config import TINYDBPATH
from tinydb import TinyDB, Query, table, where
from random import randint
import uuid

db = TinyDB(TINYDBPATH)
db.default_table_name = "notes"

query = Query()


class Test:
    def __init__(self, msg):
        self.msg = msg

    def store(self):
        db.insert({"msg": self.msg})

class Note:
    '''
        Class: Note
        Methods: 
            init => initialization, :param: id (optional)
            create_id => creates new random alphanumeric note id
            create => creates new note document, invokes create_id, pushes to DB

    '''
    def __init__(self, id=None):
        self.id = id

    def create_id(self):
        '''
            Creates custom UUID. no longer needed. 
            :returns: note_id
        '''
        id_exists = True
        while(id_exists):
            note_id = str(uuid.uuid4())
            if not db.search(query.id == note_id): id_exists = False

        return note_id

    def checks(self):
        if not self.id or not db.search(query.id == self.id):
            return False

        return True


    def create(self, content, title="New Note"):
        # content will be checked beforehand
        self.content = content
        self.title = title
        self.id = self.create_id()

        id = db.insert({
            "id": self.id,
            "title": self.title,
            "content": self.content
            })
        return self.id

    def get_note(self):

        result = db.get(query.id == self.id)

        if not result: 
            response = {"msg": "note with this id does not exist"}
        else:
            response = result 

        return jsonify(response)

    def delete_note(self):
        if not self.id: 
            response = {"msg": "no id to delete provided"}
            return jsonify(response)

        if not db.search(query.id == self.id): return jsonify({"msg": "note with this id does not exist"})

        db.remove(query.id == self.id)
        return jsonify({"msg": "item successfully deleted"})


    def edit_note(self, title, content):
        if not self.checks(): return jsonify({"msg": "no ID provided or note does not exist"})

        db.update({"content": content}, where("id") == self.id)

        if title: db.update({"title": title}, where("id") == self.id)

        return jsonify({"msg": "Edit succesful"})