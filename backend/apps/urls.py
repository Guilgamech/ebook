from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.author.views import AuthorViewSet
from apps.books.views import BookViewSet
from apps.gender.views import GenderViewSet
from apps.publishing.views import PublishingViewSet
from apps.user.views import LogoutView, UserView

router = DefaultRouter()
router.register(prefix='author', viewset=AuthorViewSet, basename='author')
router.register(prefix='gender', viewset=GenderViewSet, basename='gender')
router.register(prefix='publishing', viewset=PublishingViewSet, basename='publishing')
router.register(prefix='books', viewset=BookViewSet, basename='books')
router.register(prefix='users', viewset=UserView, basename='users')
router.register(prefix='token/logout', viewset=LogoutView, basename='token_logout')

app_name = 'api'
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
