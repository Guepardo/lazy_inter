import arrow


class Session():
    def __init__(self):
        self._started_at = None
        self._finished_at = None
        self._reason = "Simple Interruption"

    def start(self):
        self._started_at = int(arrow.now().timestamp())

    def finish(self):
        self._finished_at = int(arrow.now().timestamp())

    def add_reason(self, reason):
        self._reason = reason

    def resume(self):
        return (self._finished_at - self._started_at) / 60

    def reason(self):
        return self._reason

    def serialize(self):
        return [
            arrow.now().format('YYYY-MM-DD'),
            str(self._started_at),
            str(self._finished_at),
            self._reason
        ]
