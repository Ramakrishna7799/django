from django.db import models


class director(models.Model):
    d_name = models.CharField(max_length=50)

    def __str__(self):
        return self.d_name


class manager(models.Model):
    m_name = models.CharField(max_length=50)

    def __str__(self):
        return self.m_name


class engineer(models.Model):
    e_name = models.CharField(max_length=50)
    director = models.ForeignKey(director, on_delete=models.PROTECT)
    manager = models.ForeignKey(manager, on_delete=models.PROTECT)

    def __str__(self):
        return self.e_name
