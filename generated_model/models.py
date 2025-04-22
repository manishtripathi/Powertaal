# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Errorlog(models.Model):
    id = models.AutoField()
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


class Signuptransactiondetail(models.Model):
    transactionid = models.BigAutoField(db_column='TransactionID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Tbladvanceuser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TransactionDate', blank=True, null=True)  # Field name made lowercase.
    transactionamout = models.DecimalField(db_column='TransactionAmout', max_digits=10, decimal_places=2)  # Field name made lowercase.
    transactionrefno = models.CharField(db_column='TransactionRefNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    transactionstatus = models.BooleanField(db_column='TransactionStatus', blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='PaymentStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SignupTransactionDetail'


class Test(models.Model):
    id = models.DecimalField(db_column='Id', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Test'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Tbladminlogin(models.Model):
    id = models.AutoField(db_column='Id')  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', primary_key=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdminLogin'


class TbladvancetextEnEn(models.Model):
    adwordid = models.BigAutoField(db_column='AdWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.TextField(db_column='Language1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    language2 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    isselected = models.BooleanField(db_column='IsSelected', blank=True, null=True)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate', blank=True, null=True)  # Field name made lowercase.
    advanceuserid = models.ForeignKey('Tbladvanceuser', models.DO_NOTHING, db_column='AdvanceUserID')  # Field name made lowercase.
    meaning = models.CharField(db_column='Meaning', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdvanceText_EN_EN'


class TbladvancetextEnNl(models.Model):
    adwordid = models.BigAutoField(db_column='AdWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.TextField(db_column='Language1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    language2 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    isselected = models.BooleanField(db_column='IsSelected', blank=True, null=True)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate', blank=True, null=True)  # Field name made lowercase.
    advanceuserid = models.ForeignKey('Tbladvanceuser', models.DO_NOTHING, db_column='AdvanceUserID')  # Field name made lowercase.
    meaning = models.CharField(db_column='Meaning', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdvanceText_EN_NL'


class TbladvancetextNlEn(models.Model):
    adwordid = models.BigAutoField(db_column='AdWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.TextField(db_column='Language1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    language2 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    isselected = models.BooleanField(db_column='IsSelected', blank=True, null=True)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate', blank=True, null=True)  # Field name made lowercase.
    advanceuserid = models.ForeignKey('Tbladvanceuser', models.DO_NOTHING, db_column='AdvanceUserID')  # Field name made lowercase.
    meaning = models.CharField(db_column='Meaning', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdvanceText_NL_EN'


class TbladvancetextNlNl(models.Model):
    adwordid = models.BigAutoField(db_column='AdWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.TextField(db_column='Language1', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    language2 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    meaning = models.CharField(db_column='Meaning', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isselected = models.BooleanField(db_column='IsSelected', blank=True, null=True)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate', blank=True, null=True)  # Field name made lowercase.
    advanceuserid = models.ForeignKey('Tbladvanceuser', models.DO_NOTHING, db_column='AdvanceUserID')  # Field name made lowercase.
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdvanceText_NL_NL'


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


class Tbladvanceuserscore(models.Model):
    advanceuserscoreid = models.BigAutoField(db_column='AdvanceUserScoreID', primary_key=True)  # Field name made lowercase.
    advanceuserid = models.ForeignKey(Tbladvanceuser, models.DO_NOTHING, db_column='AdvanceUserID')  # Field name made lowercase.
    languageid = models.ForeignKey('Tbllanguage', models.DO_NOTHING, db_column='languageID')  # Field name made lowercase.
    scoreinsecond = models.IntegerField(db_column='ScoreInSecond')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdvanceUserScore'


class TbladvancewordsEnEn(models.Model):
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
        db_table = 'tblAdvanceWords_EN_EN'


class TbladvancewordsEnNl(models.Model):
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
        db_table = 'tblAdvanceWords_EN_NL'


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


class TbladvancewordsNlNl(models.Model):
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
        db_table = 'tblAdvanceWords_NL_NL'


class Tblfreeuser(models.Model):
    freeuserid = models.BigAutoField(db_column='FreeUserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    createdbysource = models.CharField(db_column='CreatedBySource', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFreeUser'


class Tblfreeuserscore(models.Model):
    freeuserscorid = models.BigAutoField(db_column='FreeUserScorID')  # Field name made lowercase.
    freeuserid = models.ForeignKey(Tblfreeuser, models.DO_NOTHING, db_column='FreeUserID')  # Field name made lowercase.
    languageid = models.ForeignKey('Tbllanguage', models.DO_NOTHING, db_column='languageID')  # Field name made lowercase.
    scorinsecond = models.IntegerField(db_column='ScorInSecond')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFreeUserScore'


class TblfreewordsEnEn(models.Model):
    freewordid = models.AutoField(db_column='FreeWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    language2 = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFreeWords_EN_EN'


class TblfreewordsEnNl(models.Model):
    freewordid = models.AutoField(db_column='FreeWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    language2 = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFreeWords_EN_NL'


class TblfreewordsNlEn(models.Model):
    freewordid = models.AutoField(db_column='FreeWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    language2 = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFreeWords_NL_EN'


class TblfreewordsNlNl(models.Model):
    freewordid = models.AutoField(db_column='FreeWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    language2 = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFreeWords_NL_NL'


class Tbllanguage(models.Model):
    languageid = models.SmallAutoField(db_column='LanguageID', primary_key=True)  # Field name made lowercase.
    languagename = models.CharField(db_column='LanguageName', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLanguage'


class TblstdwordsEnEn(models.Model):
    stdwordid = models.AutoField(db_column='STDWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    language2 = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSTDWords_EN_EN'


class TblstdwordsEnNl(models.Model):
    stdwordid = models.AutoField(db_column='STDWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    language2 = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSTDWords_EN_NL'


class TblstdwordsNlEn(models.Model):
    stdwordid = models.AutoField(db_column='STDWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    language2 = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSTDWords_NL_EN'


class TblstdwordsNlNl(models.Model):
    stdwordid = models.AutoField(db_column='STDWordID', primary_key=True)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    language2 = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    mutilangid = models.SmallIntegerField(db_column='MutiLangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSTDWords_NL_NL'
