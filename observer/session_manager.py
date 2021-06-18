from .session import Session


class SessionManager:
    _instance = None

    def __init__(self):
        self.some_attribute = None
        self.session = None

    @classmethod
    def instance(self):
        if self._instance is None:
            self._instance = self()
        return self._instance

    def start_session(self):
        session = Session()
        session.start()

        self.session = session

    def finish_session(self):
        self.session.finish()

        with open('data.csv', 'a+') as file:
            file.write(','.join(self.session.serialize()) + "\n")

    def current_session(self):
        return self.session

    def add_reason_on_current_session(self, reason):
        self.session.add_reason(reason)
