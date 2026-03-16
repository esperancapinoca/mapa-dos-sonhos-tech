from django.db import models

class Dream(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.CharField(max_length=255, blank=True, help_text="Tags separadas por vírgula, ex: #WebDesign, #Games")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Ordena os sonhos pelos mais recentes primeiro.