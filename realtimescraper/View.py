class View:

    message = ''

    def __init__(self, message):
        self.message = message

    def change_message(self, message):
        self.message = message

    def return_message(self):
        return self.message
