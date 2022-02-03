from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse(render(request, 'hello.html', status=400))


def create_brand(request):
    if request.method == 'GET':
        # TODO: render Form!
        pass
    elif request.method == 'POST':
        # TODO: Create brand!
        pass
    else:
        return HttpResponse("Invalid method!", status=405)
