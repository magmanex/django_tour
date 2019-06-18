from django.urls import path,include
from my_table import views

app_name = "my_table"

urlpatterns = [
    path(''                             , views.index               , name = 'index'),
    # path('', include(router.urls)),
    path('<int:Travel_Plan_id>'         , views.detail              , name = 'detail'),
    path('create_tour/<int:plan_id>'    , views.create_tour         , name = 'create_tour'),
    path('create_tour/create_my_table'              , views.create_my_table     , name = 'create_my_table'),
    path('create_plan'                  , views.create_plan         , name = "create_plan"),
    path('create_tour/province_in_area'             , views.province_in_area    , name = 'province_in_area'),
    path("create_tour/tour_in_province"             , views.tour_in_province    , name = "tour_in_province"),
    path('save_plan'                    , views.save_plan           , name = "save_plan"),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
