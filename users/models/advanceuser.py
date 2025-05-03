# users/models/advanceuser.py

from django.db import models

class AdvanceUser(models.Model):
    advanceuserid = models.AutoField(db_column='AdvanceuserID', primary_key=True)
    emailid = models.EmailField(db_column='Emailid')
    firstname = models.CharField(db_column='Firstname', max_length=100)
    lastname = models.CharField(db_column='Lastname', max_length=100)
    dob = models.DateField(db_column='Dob')
    mobileno = models.CharField(db_column='Mobileno', max_length=15)
    password = models.CharField(db_column='Password', max_length=255)
    place = models.CharField(db_column='Place', max_length=100)
    createddate = models.DateTimeField(db_column='CreatedDate')
    createdbysource = models.CharField(db_column='CreatedBysource', max_length=100)
    status = models.CharField(db_column='Status', max_length=50)
    enabledform = models.CharField(db_column='Enabledform', max_length=100)
    paymentref = models.CharField(db_column='PaymentRef', max_length=100)

    class Meta:
        db_table = 'tbl_advanceuser'
