class ClientMessage:
    AUTHENTICATE = 'AUTHENTICATE'
    JOIN_GROUP_TEST = 'JOIN GROUP TEST'
    GET_TEST = 'GET TEST'
    SUBMIT_TEST = 'SUBMIT TEST'

    def __init__(self):
        self.command = None
        self.detail = None

    def set_message(self, **data):
        self.command = data.get('command')
        self.detail = data.get('detail')
        return self