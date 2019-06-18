from django.test import TestCase
from .models import Area,Province,Tourist_Attraction,My_Table
from .views import province_in_area,tour_in_province
from django.urls import reverse
import json
# Create your tests here.

class TourTestCase(TestCase):
    def setUp(self):
        Area.objects.create(name="เหนือ")
        Area.objects.create(name="อีสาน")
        Area.objects.create(name="กลาง")
        Area.objects.create(name="ใต้")

        Province.objects.create(area_id=Area.objects.get(id=1),name="เชียงราย")
        Province.objects.create(area_id=Area.objects.get(id=1),name="เชียงใหม่")
        Province.objects.create(area_id=Area.objects.get(id=1),name="ลำปาง")
        Province.objects.create(area_id=Area.objects.get(id=1),name="ลำพูน")


        Tourist_Attraction.objects.create(prov_id=Province.objects.get(id=1),name="วัดร่องขุ่น")
        Tourist_Attraction.objects.create(prov_id=Province.objects.get(id=1),name="น้ำตกขุนกร")
        Tourist_Attraction.objects.create(prov_id=Province.objects.get(id=2),name="สวนสัตว์เชียงใหม่")

    def test_area(self):
        area = Area.objects.get(id=1)
        self.assertEqual(area.name , "เหนือ" , "Someting wrong on call area name")

    def test_getArea_from_tour(self):
        area = Tourist_Attraction.objects.get(id=1).prov_id.area_id.name
        self.assertEqual(area , "เหนือ" , "Someting wrong on get name of area from tour")

    def test_get_province_in_area(self):
        data = {"area_id_ref":1}
        prov = self.client.post(reverse('my_table:province_in_area') , data)
        # prov = province_in_area(area.id)
        # print(prov)
        jdata = json.loads(prov.content)
        # print(jdata)
        self.assertEqual(len(jdata),4,"Something wrong in province_in_area")
        # print(str(prov.content,encoding='utf8'))
        # self.assertEqual(len(prov),4,"Something wrong on get province from area")

    def test_get_tour_in_province(self):
        data = {"prov_id_ref":1}
        tour = self.client.post(reverse('my_table:tour_in_province') , data)
        jdata = json.loads(tour.content)
        self.assertEqual(len(jdata),2,"Something wrong on get tour from province")