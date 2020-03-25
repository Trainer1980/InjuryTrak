from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import bcrypt
import re


class UserManager(models.Manager):
    def regis_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid Email."
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty."
        data = User.objects.filter(email=postData['email'])
        if len(data) > 0:
            errors["email"] = "Email already exists, please log in."
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if postData['password'] != postData['confirm_pw']:
            errors["confirm_pw"] = "Passwords must match."
        return errors

    def pass_validator(self, postData):
        errors = {}
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if postData['password'] != postData['confirm_pw']:
            errors["confirm_pw"] = "Passwords must match."
        return errors

class AthleteManager(models.Manager):
    def ath_validator(self, postData):
        errors = {}
        if len(postData['ath_first_name']) < 2:
            errors["ath_first_name"] = "First Name should be at least 2 characters."
        if len(postData['ath_last_name']) < 2:
            errors["ath_last_name"] = "Last Name should be at least 2 characters."
        if postData['sport'] == 'none':
            errors['sport'] = "Please select a sport from the list."
        if postData['injury'] == 'none':
            errors["injury"] = "Please select an injury from the list."
        if len(postData['desc']) < 8:
            errors["desc"] = "Injury description should be at least 8 characters."
        inj_date_1 = datetime.strptime((postData['inj_date']), '%Y-%m-%d')
        if inj_date_1 > datetime.today():
            errors['inj_date'] = "Injury date must be in the past."
        poss_return_1 = datetime.strptime((postData['poss_return']), '%Y-%m-%d')
        if poss_return_1 < datetime.today():
            errors['poss_return'] = "Possible return date must be in the future."
        return errors

    def ath_update_validator(self, postData):
        errors = {}
        if len(postData['ath_first_name']) < 2:
            errors["ath_first_name"] = "First Name should be at least 2 characters."
        if len(postData['ath_last_name']) < 2:
            errors["ath_last_name"] = "Last Name should be at least 2 characters."
        if len(postData['desc']) < 8:
            errors["desc"] = "Injury description should be at least 8 characters."
        poss_return_1 = datetime.strptime((postData['poss_return']), '%Y-%m-%d')
        if poss_return_1 < datetime.today():
            errors['poss_return'] = "Possible return date must be in the future."
        return errors

class User(models.Model):
    COACH = 'Coach'
    ADMIN = 'Admin'
    S_ADMIN = 'S_Admin'
    USER_LEVEL_CHOICES = (
        (COACH, 'Coach'),
        (ADMIN, 'Admin'),
        (S_ADMIN, 'S_Admin'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    user_level = models.CharField(
        max_length=10,
        choices=USER_LEVEL_CHOICES,
        default='coach')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Athlete(models.Model):
    ARCHERY = 'Archery'
    BBASKETBALL = 'B-Basketball'
    GBASKETBALL = 'G-Basketball'
    BASEBALL = 'Baseball'
    BXCOUNTRY = 'B-XCountry'
    GXCOUNTRY = 'G-XCountry'
    FOOTBALL = 'Football'
    GOLF = 'Golf'
    GYMNASTICS = 'Gymnastics'
    BSOCCER = 'B-Soccer'
    GSOCCER = 'G-Soccer'
    SOFTBALL = 'Softball'
    SWIMMING = 'Swimming'
    TENNIS = 'Tennis'
    BTRACK = 'B-Track'
    GTRACK = 'G-Track'
    VOLLEYBALL = 'Volleyball'
    WRESTLING = 'Wrestling'
    SPORT_CHOICES = (
        (ARCHERY, 'Archery'),
        (BBASKETBALL, 'B-Basketball'),
        (GBASKETBALL, 'G-Basketball'),
        (BASEBALL, 'Baseball'),
        (BXCOUNTRY, 'B-XCountry'),
        (GXCOUNTRY, 'G-XCountry'),
        (FOOTBALL, 'Football'),
        (GOLF, 'Golf'),
        (GYMNASTICS, 'Gymnastics'),
        (BSOCCER, 'B-Soccer'),
        (GSOCCER, 'G-Soccer'),
        (SOFTBALL, 'Softball'),
        (SWIMMING, 'Swimming'),
        (TENNIS, 'Tennis'),
        (BTRACK, 'B-Track'),
        (GTRACK, 'G-Track'),
        (VOLLEYBALL, 'Volleyball'),
        (WRESTLING, 'Wrestling'),
    )

    HEAD = 'Head'
    FACE = 'Face'
    NECK = 'Neck'
    SHOULDER = 'Shoulder'
    ARM = 'Arm'
    ELBOW = 'Elbow'
    WRIST = 'Wrist'
    HAND = 'Hand'
    FINGER = 'Finger'
    CHEST = 'Chest'
    ABDOMEN = 'Abdomen'
    BACK = 'Back'
    HIP = 'Hip'
    THIGH = 'Thigh'
    KNEE = 'Knee'
    SHIN_CALF = 'Shin_Calf'
    ANKLE = 'Ankle'
    FOOT = 'Foot'
    TOE = 'Toe'
    INJURY_CHOICES = (
        (HEAD, 'Head'),
        (FACE, 'Face'),
        (NECK, 'Neck'),
        (SHOULDER, 'Shoulder'),
        (ARM, 'Arm'),
        (ELBOW, 'Elbow'),
        (WRIST, 'Wrist'),
        (HAND, 'Hand'),
        (FINGER, 'Finger'),
        (CHEST, 'Chest'),
        (ABDOMEN, 'Abdomen'),
        (BACK, 'Back'),
        (HIP, 'Hip'),
        (THIGH, 'Thigh'),
        (KNEE, 'Knee'),
        (SHIN_CALF, 'Shin_Calf'),
        (ANKLE, 'Ankle'),
        (FOOT, 'Foot'),
        (TOE, 'Toe')
    )

    ath_first_name = models.CharField(max_length=255)
    ath_last_name = models.CharField(max_length=255)
    sport = models.CharField(max_length=45, choices=SPORT_CHOICES)
    injured = models.BooleanField(default='True')
    injury = models.CharField(max_length=45, choices=INJURY_CHOICES)
    desc = models.TextField()
    inj_date = models.DateTimeField(null=True)
    poss_return = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AthleteManager()

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name='messages',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='commenter', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
