from .views import RegisterView, DisplayProfile, joinTeam, DisplayTeam, leaveTeam, UserViewSet, GroupViewSet, EsportsRegisterViewValorant, EsportsRegisterViewBGMI, EsportsRegisterViewChess, EsportsRegisterView, getAthleticEvents, getBadmintonEvents, getBasketBallEvents, getTableTennisEvents, getVolleyBallEvents
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url

app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', RegisterView.as_view(), name='register'),
    url(r'profile$', DisplayProfile, name='profile'),
    path('EsportsRegister/', EsportsRegisterView, name='EsportsRegister'),
    path(r'EsportsRegister/Valorant/', EsportsRegisterViewValorant.as_view(), name='EsportsRegisterValorant'),
    path(r'EsportsRegister/BGMI/', EsportsRegisterViewBGMI.as_view(), name='EsportsRegisterBGMI'),
    path(r'EsportsRegister/Chess/', EsportsRegisterViewChess.as_view(), name='EsportsRegisterChess'),
    url(r'^myTeam$', DisplayTeam, name='myTeam'),
    url(r'joinTeam$', joinTeam, name='joinTeam'),
    url(r'^leaveTeam$', leaveTeam, name='leaveTeam'),
    path('athletics/', getAthleticEvents, name='athleticEvents'),
    path('badminton/', getBadmintonEvents, name='badmintonEvents'),
    path('tabletennis/', getTableTennisEvents, name='tabletennisEvents'),
    path('voleyball/', getVolleyBallEvents, name='volleyballEvents'),
    path('basketball/', getBasketBallEvents, name='basketballEvents'),
]
