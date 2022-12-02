from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from geopy.distance import distance
from stream.models import Camera
from stream.serializers import CameraSerializer

from django.contrib.auth.models import User
from student.models import Student
from rest_framework import status






class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register_user(request):
    print(request.data)
    username = request.data.get("username")
    password = request.data.get("password")
    print(f'username: {username}')
    print(f'password: {password}')
    if User.objects.filter(username=username).exists():
        return Response(
            {
                'message': 'User already exists.'
            },
            status = status.HTTP_403_FORBIDDEN
            )
    else:
        User.objects.create_user(username=username, password=password)
        return Response(
            {
                "message":"Registration Successful"
                
            },
            status= status.HTTP_201_CREATED
        )








@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_cameras(request):
    user = request.user
    student = Student.objects.get(user = user)
    latitute = request.data.get('latitude')
    longitude = request.data.get('longitude')
    student.curlat = latitute
    student.curlong = longitude
    student.save()
    cameras = Camera.objects.all()
    distance_list = []
    for camera in cameras:
        d = (distance((latitute, longitude),(camera.latitude, camera.longitude)).km)*1000
        distance_list.append((camera.id, d))
    distance_list  = sorted(distance_list, key= lambda x: x[1])[:5]
    print(distance_list)
    ids = [d[0] for d in distance_list]
    candidates= [Camera.objects.get(pk=n) for n in ids]
    r = CameraSerializer(candidates, many=True)
    return Response(r.data)

      
     
    

    