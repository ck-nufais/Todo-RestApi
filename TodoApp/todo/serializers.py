from .models import Todo
from rest_framework import serializers
from django.contrib.auth.models import User
class TodoSerializers(serializers.ModelSerializer):
    time = serializers.DateTimeField(source="created",read_only=True)
    class Meta:
        model = Todo
        fields = ['id','text',"is_completed","time"]
        # another method````````````````````````````````````````
        read_only_fields = ['id']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]
        extra_kwargs = {"password":{"write_only":True}}
    def create(self,data):
        user = User.objects.create_user(
            username=data["username"],
            password=data["password"]
        )
        print(user)
        return user