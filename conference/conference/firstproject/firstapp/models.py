from django.db import models

# Create your models here.
class conference(models.Model):
    choice=[
         ('JavaScript Frameworks','JavaScript Frameworks'),
        ('JavaScript Libraries','JavaScript Libraries'),
        ('Node.js','Node.js'),
        ('Build Tools','Build Tools'),
        ('ES2015','ES2015'),
        ]
    choice2=[
        ('1 - January','1 - January'),
        ('2 - February','2 - February'),
        ('3 - March','3 - March'),
        ('4 - April','4 - April'),
        ('5 - May','5 - May'),
        ('6 - June','6 - June'),
        ('7 - July','7 - July'),
        ('8 - August','8 - August'),
        ('9 - September','9 - September'),
        ('10 - October','10 - October'),
        ('11 - November','11 - November'),
        ('12 - December','12 - December'),
    ]
    choice3=[
        ('FULL STACK JS DEVELOPER','FULL STACK JS DEVELOPER'),
        ('Front End Developer','Front End Developer'),
        ('Back End Developer','Back End Developer'),
        ('Designer','Designer'),
        ('Student','Student'),
    ]
    choice4=[
        ('2016','2016'),
        ('2017','2017'),
        ('2018','2018'),
        ('2019','2019'),
        ('2020','2020'),
        ('2021','2021'),
        ('2022','2022'),
        ('2023','2023')
    ]
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    jobRole=models.CharField(max_length=255,choices=choice3)
    topic=models.CharField(max_length=255,choices=choice)
    CardNumber=models.IntegerField()
    ZipCode=models.IntegerField()
    CVV=models.IntegerField()
    month=models.CharField(max_length=255,choices=choice2)
    year=models.CharField(max_length=255,choices=choice4)

    def id(self):
        return f"2023{self.id:04}"
    
class Speaker_management(models.Model):
     name = models.CharField(max_length=100)
     biography = models.TextField()
     photo = models.ImageField(upload_to='speakers/', blank=True, null=True)
     email = models.EmailField()
     phone_number = models.CharField(max_length=20)
     linkedin_link = models.URLField(blank=True)
     twitter_link = models.URLField(blank=True)

     def __str__(self):
        return self.name
    
class Schedule_management(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    topic = models.CharField(max_length=150)
    speaker = models.ForeignKey(Speaker_management, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.topic