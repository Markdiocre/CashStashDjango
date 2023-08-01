from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import update_last_login
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

from .serializers import IponSerializer, MoneySerializer
from .models import Ipon, Money
from .paginations import StandardResultsSetPagination

# Create your views here.
class LoginToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=result.data['token'])
        update_last_login(None, token.user)
        return result
    
class IponView(viewsets.ModelViewSet):
    queryset = Ipon.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = IponSerializer
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return super().get_queryset().filter(fld_user_id = self.request.user)
    
    def create(self, request, *args, **kwargs):
        ipon = Ipon.objects.create(
            fld_user_id = self.request.user,
            fld_ipon = request.data['fld_ipon'],
            fld_title = request.data['fld_title'],
            fld_ipon_desc = request.data['fld_ipon_desc'],
        )

        serializer = IponSerializer(ipon)
        return Response(serializer.data)
    
class IponBuyView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, format=None):
        money = Money.objects.create(
            fld_user_id = self.request.user,
            fld_value = request.data["ipon_value"],
            fld_description = request.data["ipon_description"],
            fld_type = "m",
            fld_title = "Purchased " + request.data["ipon_title"],
        )

        ipon = Ipon.objects.get(fld_ipon_id = request.data["ipon_id"]).delete()

        return Response({"message":"Succesfully deleted!"})



class MoneyView(viewsets.ModelViewSet):
    queryset = Money.objects.all().order_by('-fld_date_added')
    permission_classes = [IsAuthenticated,]
    serializer_class = MoneySerializer
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return super().get_queryset().filter(fld_user_id = self.request.user)
    
    def create(self, request, *args, **kwargs):
        model = Money.objects.create(
            fld_user_id = self.request.user,
            fld_value = request.data["fld_value"],
            fld_description = request.data["fld_description"],
            fld_type = request.data["fld_type"],
            fld_title = request.data["fld_title"],
        )
        serializer = MoneySerializer(model)

        return Response(serializer.data)
        # return super().create(request, *args, **kwargs)
    
class HomePageView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        

        minus = Money.objects.filter(fld_user_id=request.user, fld_type="m").aggregate(
            minus_count = Sum("fld_value")
        )

        add = Money.objects.filter(fld_user_id=request.user, fld_type="a").aggregate(
            add_count = Sum("fld_value")
        )

        total = float(add["add_count"] or 0) - float(minus["minus_count"] or 0)

        buyable = Ipon.objects.filter(fld_user_id=request.user, fld_ipon__lte = total)

        return Response({
            "current_pocket_money" : total,
            "recent_transactions" : MoneySerializer(Money.objects.filter(fld_user_id=request.user).order_by("-fld_date_added")[:5], many=True).data,
            "buyable" : IponSerializer(buyable, many=True).data
        })

