from pointage.settings import SECRET_KEY
from employes.models import *
from employes.serializers import *
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt , datetime

# @api_view(['GET','POST','DELETE'])
# def employes_list(request):
#         # GET list of employes
#         if request.method == 'GET':
#             cordonnes = User.objects.all()
#             cordonnes_serializer =UserSerializer(cordonnes, many=True)
#             return JsonResponse(cordonnes_serializer.data, safe=False)
#         #  POST a new employe,
#         elif request.method == 'POST':
#             data = JSONParser().parse(request)
#             tutorial_serializer =UserSerializer(data=data)
#             if tutorial_serializer.is_valid():
#                 tutorial_serializer.save()
#                 return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
#             return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # DELETE all employes
#         elif request.method == 'DELETE':
#             count = User.objects.all().delete()
#             return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        login = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=login).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token,SECRET_KEY, algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response({'status':200,'payload':serializer.data})


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response



@api_view(['GET', 'PUT', 'DELETE'])
def employes_detail(request, pk):
    # find employe by pk (id)
    try: 
            employe_pk = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
              return JsonResponse({'message': 'The employe does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        employes_serializer = UserSerializer(employe_pk) 
        return JsonResponse(employes_serializer.data) 
    
    # put a employe
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        employes_serializer = UserSerializer(employe_pk, data=data) 
        if employes_serializer.is_valid(): 
            employes_serializer.save() 
            return JsonResponse(employes_serializer.data) 
        return JsonResponse(employes_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    # delete a employe by pk
    elif request.method == 'DELETE': 
        employe_pk.delete() 
        return JsonResponse({'message': 'employe was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST','DELETE'])
def salaires(request):
        # GET list of salaires
        if request.method == 'GET':
            salaires = salaire.objects.all()
            salaires_serializer =salaireSerializer(salaires, many=True)
            return JsonResponse(salaires_serializer.data, safe=False)
        #  POST a new salaire
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            tutorial_serializer =salaireSerializer(data=data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # DELETE all salaires
        elif request.method == 'DELETE':
            count = salaire.objects.all().delete()
            return JsonResponse({'message': '{} salaires were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def employes_salaire(request, pk):
    # find salaire by pk (id)
    try: 
            salaire_pk = salaire.objects.get(pk=pk) 
    except salaire.DoesNotExist: 
              return JsonResponse({'message': 'The salary does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        salaire_serializer = salaireSerializer(salaire_pk) 
        return JsonResponse(salaire_serializer.data) 
    
    # put a salaire
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        salaire_serializer = salaireSerializer(salaire_pk, data=data) 
        if salaire_serializer.is_valid(): 
            salaire_serializer.save() 
            return JsonResponse(salaire_serializer.data) 
        return JsonResponse(salaire_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    # delete a employe by pk
    elif request.method == 'DELETE': 
        salaire_pk.delete() 
        return JsonResponse({'message': 'salaire was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET','POST','DELETE'])
def pointages(request):
        # GET list of pointage
        if request.method == 'GET':
            pointages = pointage.objects.all()
            pointage_serializer =pointageSerializer(pointages, many=True)
            return JsonResponse(pointage_serializer.data, safe=False)
        #  POST a new pointage,
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            pointage_serializer =pointageSerializer(data=data)
            if pointage_serializer.is_valid():
                pointage_serializer.save()
                return JsonResponse(pointage_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(pointage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # DELETE all pointage
        elif request.method == 'DELETE':
            count = pointage.objects.all().delete()
            return JsonResponse({'message': '{} pointage were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def employes_pointage(request, pk):
    # find pointage by pk (id)
    try: 
            pointage_pk = pointage.objects.get(pk=pk) 
    except pointage.DoesNotExist: 
              return JsonResponse({'message': 'The pointage does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        pointage_serializer = pointageSerializer(pointage_pk) 
        return JsonResponse(pointage_serializer.data) 
    
    # put a salaire
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        pointage_serializer = pointageSerializer(pointage_pk, data=data) 
        if pointage_serializer.is_valid(): 
            pointage_serializer.save() 
            return JsonResponse(pointage_serializer.data) 
        return JsonResponse(pointage_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    # delete a employe by pk
    elif request.method == 'DELETE': 
        pointage_pk.delete() 
        return JsonResponse({'message': 'pointage was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

