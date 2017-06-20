import morepath
from models import EventList, Event
from db import event_list


class App(morepath.App):
    pass


@App.path(path='')
class Root(object):
    pass


@App.html(model=Root)
def root_veiw(self, request):
    return 'Calendar test server'


@App.path(model=EventList, path='events/')
def get_list_events():
    return EventList(event_list)


@App.view(model=EventList)
def list_events(self, request):
    return self.list()


if __name__ == '__main__':
    morepath.run(App())
