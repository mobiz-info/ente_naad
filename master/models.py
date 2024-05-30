from django.db import models
import uuid


# Create your models here.

class District(models.Model):
    district_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, editable=False, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return str(self.name)


class Panchayath(models.Model):
    Panchayath_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    district = models.ForeignKey('master.District', max_length=250, null=True, blank=True, related_name='panchayath_district',
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=True, blank=False)
    
    Phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    
    user = models.ForeignKey('accounts.CustomUser', max_length=250, null=True, blank=True, related_name='panchayath_user',
                             on_delete=models.SET_NULL)
    username=models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=1024, null=True, blank=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True, default='Active')

    
   

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return str(self.name)
    

class Corporation(models.Model):
    corporation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    district = models.ForeignKey('master.District', max_length=250, null=True, blank=True, related_name='corporation_district',
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=True, blank=False)
    
    Phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    
    user = models.ForeignKey('accounts.CustomUser', max_length=250, null=True, blank=True, related_name='corporation_user',
                             on_delete=models.SET_NULL)
    username=models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=1024, null=True, blank=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True, default='Active')

    
   

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return str(self.name)
    

class Muncipality(models.Model):
    muncipality_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    district = models.ForeignKey('master.District', max_length=250, null=True, blank=True, related_name='muncipality_district',
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=True, blank=False)
    
    Phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    
    user = models.ForeignKey('accounts.CustomUser', max_length=250, null=True, blank=True, related_name='muncipality_user',
                             on_delete=models.SET_NULL)
    username=models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=1024, null=True, blank=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True, default='Active')

    
   

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return str(self.name)


class Ward(models.Model):
    ward_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    district = models.ForeignKey('master.District', max_length=250, null=True, blank=True, related_name='ward_district',
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=True, blank=False)
    
    Phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    
    user = models.ForeignKey('accounts.CustomUser', max_length=250, null=True, blank=True, related_name='ward_user',
                             on_delete=models.CASCADE)
    
    panchayath = models.ForeignKey('master.Panchayath', max_length=250, null=True, blank=True, related_name='ward_panchayath', on_delete=models.CASCADE)

    muncipality = models.ForeignKey('master.Muncipality', max_length=250, null=True, blank=True, related_name='ward_muncipality',
                             on_delete=models.CASCADE)
    corporation = models.ForeignKey('master.Corporation', max_length=250, null=True, blank=True, related_name='ward_corporation',
                             on_delete=models.CASCADE)
    
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True, default='Active')

    
   

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return str(self.name)
