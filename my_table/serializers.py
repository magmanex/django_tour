from django.contrib.auth.models import User, Group
from my_table.models import Area , Province , Tourist_Attraction , Travel_Plan , My_Table
from rest_framework import serializers


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name')

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'name', 'area')

class Tourist_AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist_Attraction
        fields = ('id', 'name' ,'province')


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel_Plan
        fields = ('id', 'name' ,'owner')

    def create(self , validated_data):
        return Travel_Plan.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance







class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserSerializer(serializers.ModelSerializer):
    travel_plan = serializers.PrimaryKeyRelatedField(many=True, queryset=Travel_Plan.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'travel_plan')
