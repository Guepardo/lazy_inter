from .session import Session
from repository.session_repository import SessionRepository


class SessionManager:
    _instance = None

    def __init__(self):
        self.some_attribute = None
        self.session = None
        self.repository = SessionRepository()

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
        self.repository.save(self.session)

    def current_session(self):
        return self.session

    def add_reason_on_current_session(self, reason):
        self.session.add_reason(reason)
