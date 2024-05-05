from rest_framework.views import Response, APIView
from rest_framework.decorators import api_view
from . import serializer as serial
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from mvt.models import Todo
from django.utils import timezone

@api_view(["POST"])
def registerUserView(request):
    try:
        serializer = serial.userSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        user = serializer.save()
        refresh = RefreshToken.for_user(user=user)
        return Response({"refresh": str(refresh), "access": str(refresh.access_token), "user": serializer.data},status=201)
    except Exception as e:
        print(e)
        return Response({"error": "server error"}, status=500)


class todoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            todo_id = request.query_params.get("id", None)
            if not todo_id is None:
                todo =  Todo.objects.get(id=todo_id, user=request.user)
                serializer = serial.todoSerializer(todo)
                return Response(serializer.data)
            todos = request.user.todos.all()
            completed_todo = todos.filter(completed=True)
            expired_todo = todos.filter(expire__lt=timezone.now())
            pending_todo = todos.filter(completed=False, expire__gt=timezone.now())
            completed_serializer = serial.todoSerializer(completed_todo, many=True)
            expired_serializer = serial.todoSerializer(expired_todo, many=True)
            pending_serializer = serial.todoSerializer(pending_todo, many=True)
            return Response({
                "compelted": completed_serializer.data,
                "expired": expired_serializer.data,
                "pending": pending_serializer.data
            })
        except Todo.DoesNotExist:
            return Response({"error": "Todo does not exist"}, status=404)
        except Exception as e:
            print(e)
            return Response({"error": "server error"}, status=500)
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = serial.todoSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
            
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        except Exception as e:
            print(e)
            return Response({"error": "server error"}, status=500)
    
    def delete(self, request, *args, **kwargs):
        try:
            todo_id = request.query_params.get("id", None)
            if todo_id is None:
                return Response({"error": "query params todo 'id' required"})
            todo =  Todo.objects.get(id=todo_id, user=request.user)
            todo.delete()
            return Response({"message": "deletion success"}, status=204)
        except Todo.DoesNotExist:
            return Response({"error": "Todo does not exist"}, status=404)
        except Exception as e:
            print(e)
            return Response({"error": "server error"}, status=500)
    
    def patch(self, request, *args, **kwargs):
        try:
            serializer = serial.todoSerializer(data=request.data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
            todo = Todo.objects.get(id=request.data.get('id'), user=request.user)
            serializer.update(instance=todo, validated_data=serializer.validated_data)
            return Response(serializer.data, status=201)
        except Todo.DoesNotExist:
            return Response({"error": "Todo does not exist"}, status=404)
        except Exception as e:
            print(e)
            return Response({"error": "server error"}, status=500)
    
@api_view(["POST"])
def makeTodoDone(request):
    try:
        todo_id = request.query_params.get("id", None)
        if todo_id is None:
            return Response({"error": "query params todo 'id' required"})
        todo = Todo.objects.get(id=todo_id, user=request.user)
        todo.completed = True
        todo.completed_at = timezone.now()
        todo.save()
        return Response({"message":"successfully marked as done"}, status=201)
    
    except Todo.DoesNotExist:
        return Response({"error": "Todo does not exist"})
    except Exception as e:
            print(e)
            return Response({"error": "server error"}, status=500)