from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LoginToken, IponView, MoneyView, HomePageView, IponBuyView

router = DefaultRouter()
router.register('ipon', IponView)
router.register('money', MoneyView)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    #Updates Login
    path('api-token-auth/', LoginToken.as_view()),


    path('home/', HomePageView.as_view()),
    path('ipon/buy/', IponBuyView.as_view()),
] + router.urls