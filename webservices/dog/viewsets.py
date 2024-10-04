from rest_framework.response import Response
from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

class DogViewSet(ModelViewSet):
    # Viewset for creating, listing, updating, retriving, and deleting our dogs
    
    #Learned I need to specifiy the serializer class that needs to be used in the class.
    serializer_class = DogSerializer
    
    def get(self, request, pk=None):
        #This gets dogs based on their primary key
        try:
            dog = Dog.objects.get(pk=pk)
        #If this dog does not exist let the user know that it's not by a 404
        except Dog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DogSerializer(dog)
        #This essentially takes the data from the dog of which was found by primary key and returns the data in JSON format
        return Response(serializer.data)
    
    def getAll(self, request):
        #GET requewsts for retrieving everything
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)
    
    def post(self, request): 
        #Handle all POST request by creating a new dog by getting the body data
        serializer = DogSerializer(data=request.data)
        #When getting data it's standard practice to vlidate the data before accessing
        if serializer.is_valid():
            #This is going to create a new instance of the Dog object
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self, request, pk=None): 
        #Handling the PUT call to the dog api
        try:
            dog = Dog.objects.get(pk=pk)
        #If this dog does not exist let the user know that it's not by a 404
        except Dog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DogSerializer(dog, data=request.data)
        #Checking is the data in the body of the request is valid
        if serializer.is_valid():
            #Updating the record in the database
            serializer.save()
            #Returning a response with the data updated
            return Response(serializer.data)
        #In the event that the dat is not valid let the user know that
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        #On a DELETE request this is the code that wil run
        try:
            dog = Dog.objects.get(pk=pk)
        #If the dog instance does not exist then return a 404 so the user knows it's not there
        except Dog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #Delete the dog from the database
        dog.delete()
        #From what I understand a successful delete is a 204
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    
class BreedViewSet(ModelViewSet):
    #This will be used for get, post, put, and delete on breed
    
    #TO call the specific serializer class
    serializer_class = BreedSerializer
    
    def get(self, request, pk=None):
        #GET requests for retrieving a record based on their primary key
        try:
            breed = Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BreedSerializer(breed)
        
    def getAll(self, request):
        #GET requewsts for retrieving everything
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        #For the POST request and creating a new breed
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        #PUT requests for breed
        try:
            #If a primary key exists we will get it based on the primary key
            breed = Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #In this case we are going to get the data with our serializer
        serializer = BreedSerializer(breed, data=request.data)
        #If the data is valid we are going to save it
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        #Handle the delete of a breed
        try:
            #If a primary key exists we will get it based on the primary key
            breed = Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #Delete the breed if it's found
        breed.delete()
        #Telling the user the delete was successful
        return Response(status=status.HTTP_204_NO_CONTENT)
        

