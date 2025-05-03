from django.db import models

class AdminLogin(models.Model):
    adminid = models.AutoField(db_column='AdminID', primary_key=True)
    username = models.CharField(db_column='Username', max_length=100)
    password = models.CharField(db_column='Password', max_length=255)

    class Meta:
        db_table = 'tblAdminLogin'
