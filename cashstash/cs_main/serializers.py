from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer as BaseUserSerializer

from .models import Ipon, Money

class IponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipon
        fields = '__all__'

class MoneySerializer(serializers.ModelSerializer):
    # current_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Money
        fields = '__all__'

    # def create(self, validated_data):
    #     user = None
    #     request = self.context.get("request")
    #     if request and hasattr(request, "user"):
    #         user = request.user

    #     return Money.objects.create(
    #         **validated_data,
    #         fld_user_id = user
    #     )

# class UserRegistrationSerializer(BaseUserRegistrationSerializer):
#     class Meta(BaseUserRegistrationSerializer.Meta):
#         fields = ('fld_fname','fld_lname', 'fld_email','username','password' ,'last_login','is_active')

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields =  ['first_name','last_name','email','username']