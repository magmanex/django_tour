from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Area,Province,Tourist_Attraction,My_Table,Travel_Plan
from django.utils import timezone
from rest_framework import viewsets , permissions , generics
from my_table.serializers import PlanSerializer , UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .permissions import IsOwner
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class PlanViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,IsOwner)
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Travel_Plan.objects.all()
    serializer_class = PlanSerializer
    search_fields = ('name')
    filter_backends = (filters.SearchFilter,)
    # filter_backends = (DjangoFilterBackend,)

    # def get_queryset(self):
    #     if self.request.method == "GET" and self.request.GET:
    #     plan = self.request.user

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
def index(request):
    travel_plan = Travel_Plan.objects.all()
    return render(request,'my_table/index.html',{'travel_plan':travel_plan})

def detail(request,Travel_Plan_id):
    my_table = My_Table.objects.filter(plan_id = Travel_Plan.objects.get(id = Travel_Plan_id))
    return render(request , 'my_table/detail.html',{'my_table':my_table , 'plan_id':Travel_Plan_id})

def create_plan(request):
    return render(request,"my_table/create_plan.html")

def create_tour(request,plan_id):
    get_area = Area.objects.all()
    get_prov = Province.objects.all()
    get_tour = Tourist_Attraction.objects.all()
    context = {'area':get_area,
               'plan_id':plan_id}
    return render(request,'my_table/create_tour.html',context)

def province_in_area(request):
    prov = Province.objects.filter(area_id=Area.objects.get(id=request.POST['area_id_ref']))
    prov_list = []
    for element in prov:
        prov_list.append({\
            "prov_id":element.id,\
            "prov_name":element.name\
        })
    return JsonResponse(prov_list, safe=False)

def tour_in_province(request):
    tour = Tourist_Attraction.objects.filter(prov_id = Province.objects.get(id=request.POST['prov_id_ref']))
    tour_list = []
    for element in tour:
        tour_list.append({\
            "tour_id":element.id,\
            "tour_name":element.name\
        })
    return JsonResponse(tour_list, safe=False)

def create_my_table(request):
    plan = Travel_Plan.objects.get(id = request.POST['plan_id'])
    test_id = Tourist_Attraction.objects.get(pk=str(request.POST['tour']))
    date_new = request.POST['tour_date']
    note = request.POST['note']
    my_table = My_Table(plan_id = plan , tour_id=test_id,date=date_new,note=note)
    my_table.save()
    return HttpResponseRedirect(reverse('my_table:detail', args=(my_table.id,)))

def save_plan(request):
    plan = Travel_Plan(name = request.POST['plan_name'])
    plan.save()
    return HttpResponseRedirect(reverse('my_table:detail', args=(plan.id,)))
