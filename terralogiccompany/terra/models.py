from django.db import models

class submit_blog(models.Model):
    CATEGORY=(
        ('Data Science','Data Science'),
        ('Cloud Computing','Cloud Computing'),
        ('Web Technology','Web Technology'),
        ('Cyber Security','Cyber Security'),
        ('Devops','Devops'),
        ('Coding','Coding')
    )
    name=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=50,null=True)
    blog_type=models.CharField(max_length=100,null=False,choices=CATEGORY)
    blog_image =models.ImageField(null=True,blank=True)
    description=models.CharField(max_length=5000,null=True)
    date_created =models.DateTimeField(auto_now_add=True,null=True)

class contact_us(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=50,null=False)
    subject=models.CharField(max_length=100,null=False)
    message=models.CharField(max_length=500,null=False)
