from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=1000)
