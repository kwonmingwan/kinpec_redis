from django.db import models

# Create your models here.
class UserModel(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_pw = models.CharField(max_length=255)
    user_nm = models.CharField(max_length=20)
    cust_cd = models.CharField(max_length=10, null=True)
    gender_ty = models.CharField(max_length=1, null=True)
    birth_dt = models.DateField(null=True)
    mobile_no = models.CharField(max_length=20)
    email_addr = models.CharField(max_length=255)
    cre_dt = models.DateTimeField(auto_now_add=True)
    cre_id = models.CharField(max_length=20, null=True)
    upt_dt = models.DateTimeField(auto_now=True)
    upt_id = models.CharField(max_length=20, null=True)

    class Meta:
        managed = False
        db_table = 'tb_user_info'
