from django.db import models

# Create your models here.
class Errorlog(models.Model):
    id = models.AutoField(primary_key=True)
    module = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(db_column='IP', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    loginid = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    stacktrace = models.TextField(db_column='stackTrace', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pageurl = models.CharField(max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ErrorLog'

    def __str__(self):
        return self.message


class Tbladvanceuser(models.Model):
    advanceuserid = models.BigAutoField(db_column='AdvanceUserID', primary_key=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    mobile = models.BigIntegerField(db_column='Mobile')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    createdbysource = models.CharField(db_column='CreatedBySource', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    enabledfrom = models.CharField(db_column='EnabledFrom', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paymentrefno = models.CharField(db_column='PaymentRefNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdvanceUser'





class TbladvancewordsNlEn(models.Model):
    adwordid = models.BigAutoField(db_column='AdWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    language2 = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    isselected = models.BooleanField(db_column='IsSelected', blank=True, null=True)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate', blank=True, null=True)  # Field name made lowercase.
    advanceuserid = models.ForeignKey(Tbladvanceuser, models.DO_NOTHING, db_column='AdvanceUserID')  # Field name made lowercase.
    meaning = models.CharField(db_column='Meaning', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdvanceWords_NL_EN'