from rest_framework import serializers
from . models import employees

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=employees
        #fields=('id,firstName','lastName')
        #firstName=serializers.CharField(max_length=100)
        fields='__all__'
