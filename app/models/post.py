import pymongo
from flask import jsonify
from datetime import date, datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]


def new_id():
    posts =list(db.posts.find())
    if not posts:
        return 1
    elif len(posts) == 1:
        return 2
    last_id = posts[len(posts) -1 ]['_id']
    return last_id +1


def set_time_now():
    return datetime.now().strftime('%d/%m/%Y %H:%M')


class Post:
    def __init__(self , title:str, author:str, tags:list, content:str):
        self._id = new_id() 
        self.created_at = set_time_now()
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content


    @staticmethod
    def get_all():
        return db.posts.find()


    @staticmethod
    def get_specific(id):
        return db.posts.find({'_id': id})


    def create_new_post(self):
      db.posts.insert_one(self.__dict__)
      return list(db.posts.find({'_id': self._id}))
      

    @staticmethod
    def delete_post(id):
        post_to_remove = list(db.posts.find({'_id':id}))
        db.posts.delete_one({'_id': id})
        return  post_to_remove

    @staticmethod
    def edit_post(id, **data):
       
        invalid_keys = []
        for key in data.keys():
            if key not in db.posts.find_one({"_id":id}).keys():
                invalid_keys.append(key)

        if invalid_keys:
            return invalid_keys

        data['updated_at'] = set_time_now()
        update = {"$set": data}
        old_post = db.posts.find_one({"_id": id})
        db.posts.update_one(old_post, update)

        return Post.get_specific(id)

    
    
    