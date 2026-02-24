from rest_framework import serializers
from .models import Student

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['name', 'email', 'password', 'department', 'year']

    def create(self, validated_data):
        name = validated_data['name']
        email = validated_data['email']
        password = validated_data['password']

        # Auto create username from email
        username = email.split('@')[0]

        user = Student.objects.create(
            username=username,
            name=name,
            email=email,
            department=validated_data['department'],
            year=validated_data['year']
        )

        user.set_password(password)
        user.save()
        return user