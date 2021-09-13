from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import serializers, models, permissions

class HelloApiView(APIView):
    """ API View de Prueba """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Retornar lista de caracteristicas del API View"""

        an_apiview = [
            "Usamos metodos HTTP como funciones (get, post, patch, put, delete)",
            "Es similar a una vista tradicional de Django",
            "Nos da el mayor control sobre la logica de nuestra aplicacion",
            "Está mapeado manuealmente a los URLs",
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Maneja actualizar un objeto """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Actualización parcial de un objeto """
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """ Borrar un objeto """
        return Response({'method':'DELETE'})

    
class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewset """
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """ Retornar Mensaje de Hola Mundo"""

        a_viewset = [
            'Usa acciones (list, create, retreve, update, partial_update)',
            'Automaticamente mapea a los URLs usando Routers',
            'Provee mas funcionalidad con menos codigo',
        ]

        return Response({'message': 'Hola!', 'a_viewset':a_viewset})

    def create(self, request):
        """ Crear nuevo mensaje de Hola Mundo """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hola {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retreve(self, request, pk=None):
        """ Obtiene un Objeto y su ID """

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Handle updating an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Hace una actualizacion parcial como patch """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Destruye un objeto """
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Crea y actualiza perfiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """ Crea tokens de autenticacion de usuario """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES