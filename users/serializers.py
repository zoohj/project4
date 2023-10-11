from rest_framework import serializers

from .models import User

class UserSeriailer(serializers.ModelSerializer):

    class Meta:
        model = User
        field = ["id", "nickname", "email",'password', 'is_staff']
        extra_kwargs= {
            'password':{'write_onle':True},
            'id':{'read_only':True},
            'is_staff':{'read_only':True},
        }