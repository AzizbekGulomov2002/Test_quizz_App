from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class TestCode(models.Model):
    SONI = (
        ('100','100 talik'),
    )
    test_code = models.CharField(max_length=400,null=True,blank=True)
    soni = models.CharField(max_length=100,choices=SONI,null=True,blank=True)
    def __str__(self):
        return self.test_code
    def save(self, *args, **kwargs):
        super(TestCode, self).save(*args, **kwargs)

        self.test_code= self.id
        super(TestCode, self).save(*args, **kwargs)
class Questions(models.Model):
    test = models.ForeignKey(TestCode,on_delete=models.CASCADE)
    question_id = models.UUIDField(primary_key=True,default=uuid.uuid1,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.TextField(verbose_name="Savol",help_text="Savol kiriting")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Questions'
        verbose_name = "Savol "
        verbose_name_plural = "Savollar  "
    def __str__(self):
        element = self.question
        return f"{element[10:]}..."
class Answers(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer = models.TextField(verbose_name="Javob",help_text="Javob kiriting")
    status = models.BooleanField(default=False,verbose_name="Javob to'g'ri yoki Noto'g'ri",help_text="Javob statusi")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Answers'
        verbose_name = "Javob "
        verbose_name_plural = "Javoblar  "
    # def __str__(self):
    #     element = self.answer
    #     return f"{element[10:]}..."
    