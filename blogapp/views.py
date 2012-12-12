from django.http import HttpResponse

def hello_world(request):
    x=1234
    import code; code.interact(local=locals())
    return HttpResponse("hello world, from philip!!")
    