from rest_framework.decorators import api_view
from rest_framework.response import Response
from Users.models import User
from Users.serializers import UserSerializer


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if User.objects.filter(username=username, password=password).exists():
        user = User.objects.get(username=username, password=password)
        serializer = UserSerializer(user)
        return Response({'code': 0, 'message': '登陆成功', 'data': {serializer.data}})


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'code': 1, 'message': '用户名已存在', 'data': {}})
    else:
        user = User.objects.create(username=username, password=password)
        serializer = UserSerializer(user)
        return Response({'code': 0, 'message': '注册成功', 'data': {serializer.data}})
