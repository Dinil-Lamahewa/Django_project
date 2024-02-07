from django.db import models

class School(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class AssessmentArea(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=255)

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    summary = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class SydneyParticipant(models.Model):
    participant = models.ForeignKey(Student, on_delete=models.CASCADE)
    syndey_percentile = models.FloatField()
    assessment_area = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)

class Award(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

class CorrectAnswerPercentagePerClass(models.Model):
    assessment_area = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_percentage = models.FloatField()

class AnswerSummary(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    correct_answer = models.ForeignKey('CorrectAnswer', on_delete=models.CASCADE)

class CorrectAnswer(models.Model):
    answer_summary = models.OneToOneField(AnswerSummary, on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class YearLevelName(models.Model):
    name = models.CharField(max_length=255)