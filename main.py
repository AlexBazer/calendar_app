import morepath
import gcalendar
from models import EventList, Event, ResourceList, Resource, Subscibe
from db import event_list, resouce_list


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


@App.path(model=Event, path='/events/{pk}')
def get_event(pk):
    return EventList(event_list).get(pk)


@App.path(model=ResourceList, path='resources/')
def get_list_resources():
    return ResourceList(resouce_list)


@App.path(model=Subscibe, path='subscribe/events')
def get_subscribe_events():
    return Subscibe()


@App.view(model=EventList)
def list_events(self, request):
    return self.list()


@App.view(model=Event)
def event(self, request):
    return str(self)


@App.view(model=ResourceList)
def list_resources(self, request):
    return self.list()


@App.view(model=ResourceList, request_method='POST')
def create_resource(self, request):
    self.add(request.headers)
    return "OK"


@App.html(model=Subscibe, request_method='POST')
def subscribe_for_events(self, request):
    api = gcalendar.get_api('keyfile.json')
    result = gcalendar.subscribe_for_events(api, 'resources/')
    return str(result)


app = App()

if __name__ == '__main__':
    morepath.run(app)
