from django.shortcuts import render,HttpResponse
from todo.models import TodoModel
from todo.serializers import TaskSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return HttpResponse('hello')


####function based viewes
@api_view(['GET','POST'])
def todoList(request):
    if request.method =="GET":
        try:
            todo = TodoModel.objects.all()
            if not todo.exists():
                raise TodoModel.DoesNotExist
            serializer= TaskSerializers(todo, many=True)
            print("\n serializer data: ", serializer.data)
            return Response(
            {'data':serializer.data,'message':'todos are fetched successfully!!!!'},
            status=status.HTTP_200_OK
            )

        except TodoModel.DoesNotExist as e:
           
            return Response({"error":"data not found"},status=status.HTTP_404_NOT_FOUND)  

        except Exception as e:
            print('error : ',e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    if request.method =="POST":
        try:
            print('request data : ', request.data)
            serializer= TaskSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'data':serializer.data,
                'message':'todo added successfully'
            },
            status=status.HTTP_201_CREATED)
        except Exception as e:
            print('error',e)
            return Response({
                'error':'error while adding todos',

            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
###utility function
def getTodo(pk):
        try:
            todo = TodoModel.objects.get(pk=pk)
            return todo
        
        except TodoModel.DoesNotExist:
            return Response({'error':'data not found'},status=status.HTTP_404_NOT_FOUND)
        

@api_view(['GET',"PATCH","DELETE"])
def todoDetails(request,pk):
   
    if request.method=="GET":
        todo = getTodo(pk)
        print('todo data we are getting is : ',todo)
        if isinstance(todo,Response):    ###this isinstance method check whether we are getting instance of data or Response from the database
                                        ###Response actually we get when model instance is not found, it returns with Response objects with errors
            return todo    #### here we are checking the falsi value so this will execute when the statement is false
        
        serializer = TaskSerializers(todo)
        return Response(serializer.data)

    if request.method == "PATCH":
        todo= getTodo(pk)
        if isinstance(todo,Response):
            return todo
        todo.status= not todo.status
        todo.save()
        serializer = TaskSerializers(todo)
        return Response({
            'data':serializer.data,
            'message':'status updated successfully'
        },
        status=status.HTTP_200_OK
        )

    if request.method =="DELETE":
        data = getTodo(pk=pk)
        print(data)
        if isinstance(data,Response):
            return data
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    