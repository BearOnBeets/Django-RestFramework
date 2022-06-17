from rest_framework import serializers
from .models import Student,University

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model=University
        fields=('university_name','location')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    university = UniversitySerializer()
    class Meta:
        model=Student
        fields=('url','name','course','grade','university')
    

    def create(self,validated_data):
        u=validated_data.pop('university')
        try:
            university=University.objects.get(university_name=u['university_name'],location=u['location'])
        except University.DoesNotExist:
            raise serializers.ValidationError("Entered University DoesNot exist")
        student=Student.objects.create(**validated_data,university=university)
        return student

    def update(self,instance,validated_data):
        u=validated_data.pop('university')
        try:
            university=University.objects.get(university_name=u['university_name'],location=u['location'])
        except University.DoesNotExist:
            raise serializers.ValidationError("Entered University DoesNot exist")

        instance.name = validated_data.get('name', instance.name)
        instance.course= validated_data.get('course', instance.course)
        instance.grade=validated_data.get('grade', instance.grade)
        instance.university.university_name=u.get('university_name',instance.university.university_name)
        instance.university.location=u.get('location',instance.university.location)
        instance.save()
        return instance
