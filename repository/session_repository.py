import os


class SessionRepository:
    DATABASE_NAME = 'data.csv'

    def __init__(self):
        self.init_database()

    def path_database_folder(self):
        return f"{os.path.expanduser('~')}/.lazy_interruption"

    def full_path_database(self):
        return f"{self.path_database_folder()}/{self.DATABASE_NAME}"

    def init_database(self):
        if os.path.exists(self.path_database_folder()):
            return

        os.mkdir(self.path_database_folder())

    def save(self, session):
        with open(self.full_path_database(), 'a+') as file:
            file.write(','.join(session.serialize()) + "\n")
