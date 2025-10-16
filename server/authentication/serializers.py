from .models import User
from utils.exception.exception import CustomException as ce 
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class UserRegistrationSerailizer(serializers.ModelSerializer):
    password=serializers.CharField(
        write_only=True,
        style={'input_type':'password'},
        validators=[validate_password]
    )
    password_confirmation=serializers.CharField(
        write_only=True,
        style={'input_type':'password'},
        validators=[validate_password]
    )


    class Meta:
        model=User 
        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password_confirmation'
        ]


    def validate(self, attrs):
        """
        Validating two passwords field
        """
        password=attrs.get('password')
        password_confirmation=attrs.get('password_confirmation')

        if password!=password_confirmation:
            raise ce(
                message="Form Validation Error",
                error={
                "password": [
                        "Two Passwords Doesn't match."
                ],
                "password_confirmation": [
                        "Two Passwords Doesn't match."
                ]
                }
            )
        return attrs 
    

    def create(self,validated_data):
        """
        Over-riding the create method to create a user
        account 
        """
        try:       
            user=User.objects.create(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                username=validated_data['username'],
                email=validated_data['email'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user 
            
        except Exception as e:
            raise ce(
                message="Some Error occoured during registration"
            )
        

class UserLoginSerailizer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(
        write_only=True,
        style={'input_type':'password'},
    )


class UserChangePasswordSerailizer(serializers.Serializer):
    old_password=serializers.CharField(
        write_only=True,
        style={'input_type':'password'},
    )
    new_password=serializers.CharField(
        write_only=True,
        style={'input_type':'password'},
        validators=[validate_password]
    )
    new_password_confirmation=serializers.CharField(
        write_only=True,
        style={'input_type':'password'},
        validators=[validate_password]
    )


    def validate_old_password(self,value):
        """
        Validation for Checking if old password matches or not 
        """
        user=self.context['user']
        
        if not user.check_password(value):
            raise ce(
                message="Your current password doesn't match",
                )
        
        return value
    

    def validate(self, attrs):
        """
        Extra Validation of New Password and Old Password
        with New Password
        """
        old_password=attrs.get('old_password')
        new_password=attrs.get('new_password')
        new_password_confirmation=attrs.get('new_password_confirmation')

        if new_password != new_password_confirmation:
            raise ce(
                message='Two Passwords does not match'
            )
        
        if old_password==new_password:
            raise ce(
                message="New passwords cannot be similar to current password "
            ) 
        
        user=self.context['user']
        user.set_password(new_password)
        user.save()
        return attrs 





    




    


    
    
    



