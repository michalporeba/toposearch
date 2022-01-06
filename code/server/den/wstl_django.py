from .wstl import Wstl, WstlContextProvider
from django.urls import get_resolver
#from django.conf import settings
from django_kinder_settings import settings

    # Do something
class DjangoWstlContextProvider(WstlContextProvider):
    def get_action_url(self, name: str) ->str:
        urls = get_resolver().reverse_dict
        if name in urls.keys():
            (data, b, c, d) = urls[name]
            if len(data)>0:
                (url, pattern) = data[0]
                return settings.KinderSettings.get('hello')
                #return settings.DEFAULT_ROOT_URL+url
        return None            

        

