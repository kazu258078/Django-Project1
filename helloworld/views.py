#viewはrequestを受けとり、responseを返す

from django.http import HttpResponse
from django.views.generic.base import TemplateView


# function based View
def helloworldfunction(request):
    returnobject = HttpResponse("<h1>Hellow world</h1>")
    return returnobject
    #retunn None: responseを返してないからエラーになる


# Class based View
class HelloWorldView(TemplateView):
    template_name = 'hello.html'