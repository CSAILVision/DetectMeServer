from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Box
from .serializers import BoxSerializer

@api_view(['GET', 'POST'])
def box_list(request):
    """
    List all boxes, or create a new box.
    """
    if request.method == 'GET':
        boxes = Box.objects.all()
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BoxSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def box_detail(request, pk):
    """
    Retrieve, update or delete a box.
    """
    try:
        box = Box.objects.get(pk=pk)
    except Box.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BoxSerializer(box)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BoxSerializer(box, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        box.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET',])
def box_last(request, timestamp):
	"""
	Retrieve all the boxes greater than the timestamp
	"""
	last_boxes = Box.objects.filter(created__gte=timestamp)
	serializer = BoxSerializer(last_boxes, many=True)
	return Response(serializer.data)


