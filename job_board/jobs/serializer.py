from rest_framework import serializers
from django.contrib.auth.models import User
from jobs.models import Industries,JobPost,Company,Review,Application
from fuzzywuzzy import fuzz
from nltk import word_tokenize

## Serializers

'''class Industyserializers(serializers.Serializer):
    Id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=200)

    class Meta:
        fields = ['Id' , 'name']
    def create(self, validated_data):
        return Industries.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name  = validated_data.get("name", instance.name)
        instance.save()
        return instance

class Companyserializers(serializers.Serializer):
    Id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    industries = Industyserializers(many = True)

    class Meta:
        fields = ['Id', 'name','location', 'industries']
    def create(self, validated_data):
        return Companyserializers.objects.create(**validated_data)

class JobPostserializers(serializers.Serializer):
    Id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    company = Companyserializers()
    created_at = serializers.DateTimeField(required = False)

    class Meta:
        fields = ['Id','title','description','created_at']

    def create(self, validated_data):
        return JobPost.objects.create(**validated_data)
        

class Reviewserializers(serializers.Serializer):
    Id = serializers.IntegerField(read_only = True)
    company = Companyserializers()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Foreign key to User
    rating = serializers.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating from 1 to 5
    comment = serializers.CharField(max_length = 500)
    created_at = serializers.DateTimeField(read_only = True)

class Applicationserializers(serializers.Serializer):
    Id = serializers.IntegerField(read_only = True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Foreign key to User
    job_post = JobPostserializers()
    applied_on = serializers.DateTimeField(read_only = True)'''


## Model Serializers


class Industyserializers(serializers.ModelSerializer):

    #nam_length = serializers.SerializerMethodField( source = "name_length", required = False, read_only = True)
    name_fuzz = serializers.SerializerMethodField()
    name_word_tokenize = serializers.SerializerMethodField()

    class Meta:
        model = Industries
        fields = ['id','name','name_fuzz','name_word_tokenize']
        #fields ="__all__" serialize all field
        # exclude = ["name"] don't want to serialize
        extra_kwargs = {"id" : {"read_only" : True}}

    def validate_name(self, name):

        if len(name) <= 5:
            raise serializers.ValidationError("Name should be greater than 5")
        return name
    
    def get_name_fuzz(self,obj):
        return fuzz.ratio(obj.name , "on")
    
    def get_name_word_tokenize(self,obj):
        return word_tokenize(obj.name)
    
    def to_internal_value(self, data):
        print("check internal_value")
        return super().to_internal_value(data)
    
    def run_validation(self, data):
        print("check run_validation")
        return super().run_validation(data)
    
    def to_representation(self, instance):
        print("check representation")
        ret = super().to_representation(instance)
        ret['name'] = ret['name'].upper()
        return ret
    
class Reviewserializers(serializers.ModelSerializer):

    review_location = serializers.CharField(source = "company.location" , required = False, read_only = True )
    company_review_len = serializers.IntegerField(source = "review_length", required = False, read_only = True)

    class Meta:

        model = Review
        fields = ['company', 'user', 'rating', 'comment', 'created_at', 'review_location', 'company_review_len']
    
class Companyserializers(serializers.ModelSerializer):
    
    # Nested Serializer
    company_review = Reviewserializers(source = "reviews" , many = True, read_only = True)
    
    class Meta:

        model = Company
        fields = ['name','location','industries', 'company_review']

class JobPostserializers(serializers.ModelSerializer):
    
    class Meta:

        model = JobPost
        fields = '__all__'


class Applicationserializers(serializers.ModelSerializer):

    class Meta:

        model = Application
        fields = '__all__'


        
