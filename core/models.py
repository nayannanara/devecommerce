from django.db import models
from django.core.mail import send_mail

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=40, verbose_name='Nome')
    email = models.EmailField(max_length=40, verbose_name='Email')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    mensagem = models.TextField(verbose_name='Mensagem')

    def save(self, *args, **kwargs):
        nome = self.nome
        email = self.email
        telefone = self.telefone
        mensagem = self.mensagem
        msg = 'Nome: {0}\nE-mail: {1}\nCelular: {2}\nMensagem: {3}\n'.format(nome, email, telefone, mensagem)
        super(Contato, self).save(*args, **kwargs)
        send_mail(
            'Contato | Django Ecommerce',
            msg,
            'nayannadeveloper@gmail.com',
            ['nayannadeveloper@gmail.com'],
            fail_silently=False,
        )

    def __str__(self):
        return self.nome
