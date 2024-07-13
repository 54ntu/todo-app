from todo.models import TodoModel
from rest_framework import serializers

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields= ('id','task','status',)