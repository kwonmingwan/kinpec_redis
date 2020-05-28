from django.shortcuts import render
import bcrypt
import jwt
import logging
logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.http import QueryDict

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from api_user.models import UserModel
from api_user.serializers import UserModelSerializer

from django.shortcuts import get_object_or_404

# [CBV] - Class based views - 클래스기반 (APIView)
"""
API 사용자조회
API 사용자등록
API 사용자전체삭제
"""
class UserListAction(APIView):
    def get(self, request):
        logger.debug('UserListAction() = {}'.format("List"))
        user_list = UserModel.objects.all()
        user_list_serializer = UserModelSerializer(user_list, many=True)

        return JsonResponse(user_list_serializer.data, safe=False)

    def post(self, request):
        user_json = JSONParser().parse(request)
        user_json['user_pw'] = bcrypt.hashpw(user_json['user_pw'].encode('UTF-8'), bcrypt.gensalt()).decode('UTF-8')
        user_json['cre_id'] = 'admin'
        user_json['upt_id'] = 'admin'

        user_serializer = UserModelSerializer(data=user_json)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)