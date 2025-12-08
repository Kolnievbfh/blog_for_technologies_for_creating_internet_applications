from django.db import models

class Review(models.Model):
    full_name = models.CharField("ФИО", max_length=120)
    email = models.EmailField("Email")
    text = models.TextField("Текст отзыва")
    checked = models.BooleanField("Проверено", default=False)

    def __str__(self):
        return f"{self.full_name} — {'Проверено' if self.checked else 'Не проверено'}"
