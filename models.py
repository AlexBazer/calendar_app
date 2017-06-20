class EventList(object):
    def __init__(self, db_events):
        self.events = {key: Event(value) for key, value in db_events.items()}

    def add(self, event):
        self.events[event.event_id] = event

    def list(self):
        return '\n'.join('{}: {}'.format(key, str(value)) for key, value in self.events.items())


class Event(object):
    id = None
    title = None
    dtime = None
    calendar_id = None

    def __init__(self, db_event):
        self.id = db_event.id
        self.title = db_event.title
        self.dtime = db_event.dtime
        self.calendar_id = db_event.calendar_id

    def __str__(self):
        return '{} at {}'.format(self.title, self.dtime.isoformat())
