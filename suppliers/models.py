from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)   #CRIAÇÃO DA TABELA
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']     #ORDENAÇÃO POR NOME

    def __str__(self):
        return self.name        #REPRESENTAR A STRING DA BRAND POR NOME