from chef_chantier.models import *
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from chef_chantier.serializers import *
from rest_framework.parsers import JSONParser 
from rest_framework import status

@api_view(['GET','POST','DELETE'])
def missions(request):
        # GET list of missions
        if request.method == 'GET':
            missions = mission.objects.all()
            missions_serializer =missionsSerializer(missions, many=True)
            return JsonResponse(missions_serializer.data, safe=False)

        #  POST a new mission,
        if request.method == 'POST':
            data = JSONParser().parse(request)
            missions_serializer = missionsSerializer(data=data)
            if missions_serializer.is_valid():
                missions_serializer.save()
                return JsonResponse(missions_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(missions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # DELETE all missions
        elif request.method == 'DELETE':
            count = mission.objects.all().delete()
            return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def mission_detail(request, pk):
    # find mission by pk (id)
    try: 
            mission_pk = mission.objects.get(pk=pk) 
    except mission.DoesNotExist: 
              return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        missions_serializer = missionsSerializer(mission_pk) 
        return JsonResponse(missions_serializer.data) 
    
    # put a mission
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        missions_serializer = missionsSerializer(mission_pk, data=data) 
        if missions_serializer.is_valid(): 
            missions_serializer.save() 
            return JsonResponse(missions_serializer.data) 
        return JsonResponse(missions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    # delete a mission by pk
    elif request.method == 'DELETE': 
        mission_pk.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
