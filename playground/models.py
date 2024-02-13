from django.db import models

# Create your models here.
class airport_list(models.Model):
    code=models.AutoField(primary_key=True)  # This is the default primary key
    name=models.CharField(max_length=100)
    # airport_code=models.CharField(max_length=10,db_column='class')
    class Meta:
        db_table='airport_list'

# Create your models here.
class flight(models.Model):
    id = models.AutoField(primary_key=True)  # This is the default primary key
    airline_name=models.CharField(max_length=100)
    # airport_code=models.CharField(max_length=10,db_column='class')
    class Meta:
        db_table='flight'