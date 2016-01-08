from __future__ import unicode_literals

from storage.mongo import mongoclient


class User(object):
    id
    first_name
    last_name
    photos
    about_me

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('_id')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.photos = kwags.get('photos', [])
        self.about_me = kwargs.get('about_me', '')

    def save(self):
        result = mongoclient.users.insert_one(self.bson())
        self.id = result.inserted_id

    def delete(self):
        mongoclient.users.delete({'id': self.id})

    @classmethod
    def get_users_by_uids(cls, uids):
        mongo_users = mongoclient.find({'_id': {'$in': uids}})
        users = [cls(**mongo_user) for mongo_user in mongo_users]
        return users
