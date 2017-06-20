from collections import namedtuple
from datetime import datetime, timedelta


Event = namedtuple('Event', ('id', 'title', 'dtime', 'calendar_id'))


now = datetime.now()
event_list = {
    i: Event(str(i), 'Event' + str(i), now + timedelta(hours=1), 'i') for i in range(1, 10)
}

resouce_list = []
