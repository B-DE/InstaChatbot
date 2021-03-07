from rest_framework import serializers
from .models import Customers, Collections, Post_analysis, Modifier, Business

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('name', 'customer_id', 'password', 'instagram_id', 'instagram_pw')

class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ('customer_id', 'post_id')

class Post_analysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_analysis
        fields = ('post_id', 'business_name', 'sector', 'region', 'modifier')

class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = ('modifier_id', 'modifier')

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields =('business_id', 'address', 'call_number')