from django.middleware.csrf import rotate_token
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework import status
from utils.check_login import user_permission,user_authentication

# Create your views here.

# 登陆之前获取csrftoken
class CsrfTokenView(APIView):
    def get(self,request):
        request.META["CSRF_TOKEN"] = rotate_token(request)

        return Response({"message":"ok"},status=status.HTTP_200_OK)

# 用户登陆界面
class UserLoginViews(APIView):
    def post(self, request):
        # 获取用户信息
        data = request.data
        username = data.get("username")
        password = data.get("password")

        # 判断用户名密码是否存在
        if not username or not password:
            return Response({"message": "用户名密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)

        # 查询数据库
        try:
            user = User.objects.filter(username=username).first()
        except User.DoesNotExist:
            return Response({"message": "用户不存在"}, status=status.HTTP_400_BAD_REQUEST)
        # 判断用户是否存在
        if not user:
            # 用户不存在
            return Response({"message": "用户不存在"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 用户存在,判断用户密码是否正确
            if not user.password == password:
                return Response({"message":"密码错误"}, status=status.HTTP_400_BAD_REQUEST)
            # 用户密码正确,登陆成功
            # 设置cookie,session
            request.session["user_name"] = user.username
            request.session["is_login"] = True


            response = Response({"登陆成功"}, status=status.HTTP_200_OK)
            response.set_cookie(key="servername",value="ai.jygoal.com",max_age=3600,path="/#")

            return response

# 用户名存在性校验
class UserNameCheckView(APIView):
    def post(self,request):
        userName = request.data.get("userName")
        # 参数校验
        if not userName:
            return Response({"message": "用户名密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)
        # 查询数据库该用户是否已经注册过
        try:
            user = User.objects.filter(username=userName).first()
            userRegister = UserRegister.objects.filter(username=userName).first()
        except User.DoesNotExist:
            return Response({"message": "用户不存在"}, status=status.HTTP_400_BAD_REQUEST)
        # 用户已经存在
        if user or userRegister:
            return Response({"message": "该用户名已经注册，请勿重复注册"}, status=status.HTTP_400_BAD_REQUEST)
        # 用户名未被占用
        return Response({"message": "ok"}, status=status.HTTP_200_OK)
#
# # 用户注册页面
# class UserRegisterView(APIView):
#     def post(self,request):
#         userName = request.data.get("userName")
#         passWord = request.data.get("passWord")
#         mobile = request.data.get("mobile")
#
#         # 判断用户名密码是否存在
#         if not userName or not passWord:
#             return Response({"message": "用户名密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)
#
#         # 判断手机号是否存在
#         if not mobile:
#             return Response({"message": "手机号是否存在"}, status=status.HTTP_400_BAD_REQUEST)
#
#         # 用户注册
#         try:
#             userRegister = UserRegister(username=userName,password=passWord,mobile=mobile)
#             userRegister.save()
#         except Exception as e:
#             return Response({"message": "注册失败"}, status=status.HTTP_400_BAD_REQUEST)
#
#         return Response({"message": "注册成功"}, status=status.HTTP_200_OK)

# 用户密码修改
class PasswordModify(APIView):
    def post(self,request):
        # 获取参数
        username = request.data.get("username")
        password = request.data.get("password")
        # 参数校验

        pass



# 管理员登陆界面
class AdminLoginViews(APIView):
    def post(self,request):

        # 获取用户名和密码
        username = request.data.get("username")
        password = request.data.get("password")

        # 参数校验
        if not all([username,password]):
            return Response({"message": "用户名密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)

        # 查询数据库
        try:
            user = User.objects.filter(username=username).first()
        except User.DoesNotExist:
            return Response({"message": "用户不存在"}, status=status.HTTP_400_BAD_REQUEST)
        # 判断用户是否存在
        if not user:
            # 用户不存在
            return Response({"message": "用户不存在"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 判断用户身份
            if user.IsAdmin != 1:
                return Response({"message": "无权限登陆"}, status=status.HTTP_400_BAD_REQUEST)

            # 用户存在,判断用户密码是否正确
            if not user.password == password:
                return Response({"message": "密码错误"}, status=status.HTTP_400_BAD_REQUEST)
            # 用户密码正确,登陆成功
            # 设置cookie,session
            request.session["user_name"] = user.username
            request.session["is_login"] = True

            response = Response({"登陆成功"}, status=status.HTTP_200_OK)
            response.set_cookie(key="servername", value="ai.jygoal.com", max_age=3600, path="/#")

            return response




