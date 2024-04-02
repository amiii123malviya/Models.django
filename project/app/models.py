from django.db import models

# Create your models here.
class Student (models.Model):
    Stu_name=models.CharField(max_length=50)
    Stu_Email=models.EmailField()
    Stu_Contact=models.IntegerField()
    Stu_Add=models.CharField(max_length=100)
    Stu_city=models.CharField(max_length=50,null=True)

    class Meta:#meta class is used chnaging the behaviour of class 

        # ordering=["Stu_name"]#it will list the data in assending order
        ordering=["-Stu_name"]#it will list the data in decending order

        # verbose_name="stu" #this is we are using for chnaging the name of class but it will come with 's' 
        #verbose_name_plural="stu"# if we dont want the name of the class with 's' we use this command
        db_table='stu_table'#to chage the name of our table in db.sqlite 
        get_latest_by="Name"