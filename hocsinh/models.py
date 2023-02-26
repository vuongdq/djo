from django.db import models

class HocSinh(models.Model):
    MA_HOC_SINH = models.CharField(max_length=10, primary_key=True)
    HO_TEN = models.CharField(max_length=100)
    NGAY_SINH = models.DateField()
    GIOI_TINH = models.BooleanField()
    DIA_CHI = models.CharField(max_length=200)

    def __str__(self):
        return self.HO_TEN
