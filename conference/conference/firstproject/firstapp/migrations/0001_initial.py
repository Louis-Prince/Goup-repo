# Generated by Django 4.2.2 on 2023-07-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('jobRole', models.CharField(choices=[('FULL STACK JS DEVELOPER', 'FULL STACK JS DEVELOPER'), ('Front End Developer', 'Front End Developer'), ('Back End Developer', 'Back End Developer'), ('Designer', 'Designer'), ('Student', 'Student')], max_length=255)),
                ('topic', models.CharField(choices=[('JavaScript Frameworks', 'JavaScript Frameworks'), ('JavaScript Libraries', 'JavaScript Libraries'), ('Node.js', 'Node.js'), ('Build Tools', 'Build Tools'), ('ES2015', 'ES2015')], max_length=255)),
                ('CardNumber', models.IntegerField()),
                ('ZipCode', models.IntegerField()),
                ('CVV', models.IntegerField()),
                ('month', models.CharField(choices=[('1 - January', '1 - January'), ('2 - February', '2 - February'), ('3 - March', '3 - March'), ('4 - April', '4 - April'), ('5 - May', '5 - May'), ('6 - June', '6 - June'), ('7 - July', '7 - July'), ('8 - August', '8 - August'), ('9 - September', '9 - September'), ('10 - October', '10 - October'), ('11 - November', '11 - November'), ('12 - December', '12 - December')], max_length=255)),
                ('year', models.CharField(choices=[('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')], max_length=255)),
            ],
        ),
    ]
