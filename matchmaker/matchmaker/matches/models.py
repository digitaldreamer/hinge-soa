from __future__ import unicode_literals

from storage.mongo import mongoclient


class Match(object):
    id
    users
    state
    STATES = {
        'potential': 0,
        'match': 1,
        'blocked': 2,
    }

    def __init__(self, users, *args, **kwargs):
        """
        users - a list the uid pair: [uid1, uid2]
        """
        self.id = kwargs.get('_id')
        self.users = users
        self.state = Match.STATES[kwargs.get('potential', 0)]

    def save(self):
        result = mongoclient.matches.insert_one(self.bson())
        self.id = result.inserted_id

    def delete(self):
        mongoclient.matches.delete({'id': self.id})

    def subject_id(self, player_uid):
        """
        return the uid of the subject
        """
        if self.users[0] == player_uid:
            subject_uid = self.users[1]
        else:
            subject_uid = self.users[0]

        return subject_uid

    @classmethod
    def get_by_id(cls, id_):
        mongo_data = mongoclient.get({'_id': id_})
        match = cls(**mongo_data)
        return match

    @classmethod
    def get_matches(cls, uid=None, state=None):
        query = {}
        matches = []

        if uid:
            query['users'] = {'$in': [uid]}
        if state:
            query['state'] = STATE[state]

        mongo_matches = mongoclient.find(query)

        for mongo_match in mongo_matches:
            match = cls(**mongo_match)
            matches.append(match)

        return matches

    @classmethod
    def create(cls, *args, **kwargs):
        match = cls(*args, **kwargs)
        match.save()
        return match
