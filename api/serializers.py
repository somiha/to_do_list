from rest_framework import serializers
from .models import Task
		
class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'


class TaskSerializerOnlyTask(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('title','id', 'completed')


class TaskSerializerUpdate(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('title','id', 'completed')
