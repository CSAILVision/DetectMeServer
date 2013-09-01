from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Box
from .serializers import BoxSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def box_list(request):
    """
    List all boxes, or create a new box.
    """
    if request.method == 'GET':
        boxes = Box.objects.all()
        serializer = BoxSerializer(boxes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoxSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def box_detail(request, pk):
    """
    Retrieve, update or delete a box.
    """
    try:
        box = Box.objects.get(pk=pk)
    except Box.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BoxSerializer(box)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BoxSerializer(box, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        box.delete()
        return HttpResponse(status=204)

@csrf_exempt
def box_last(request, timestamp):
	"""
	Retrieve all the boxes greater than the timestamp
	"""
	last_boxes = Box.objects.filter(created__gte=timestamp)
	serializer = BoxSerializer(last_boxes, many=ture)
	return JSONResponse(serializer.data)