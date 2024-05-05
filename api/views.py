from rest_framework.views import Response
from rest_framework.decorators import api_view
from . import serializer as serial
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(["POST"])
def registerUserView(request):
    serializer = serial.userSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    user = serializer.save()
    refresh = RefreshToken.for_user(user=user)
    return Response({"refresh": str(refresh), "access": str(refresh.access_token), "user": serializer.data},status=201)