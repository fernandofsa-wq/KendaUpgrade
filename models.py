

from django.contrib.auth.models import User
from django.db import models


class Sliders(models.Model):
    titulo = models.CharField(max_length=65)
    subtitulo = models.CharField(max_length=120)
    coverweb = models.ImageField(
        upload_to='homepage/slider/%Y/%m/%d/', blank=True, default=''
    )
    covermobile = models.ImageField(
        upload_to='homepage/slider/%Y/%m/%d/', blank=True, default=''
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name_plural = '1.2) Sliders'

    def __str__(self):
        return self.titulo


class Patrocinio(models.Model):
    patrocinador = models.CharField(max_length=50)
    img = models.ImageField(upload_to='homepage/patrocinio/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    website = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name_plural = '1.4) Patrocinios'

    def __str__(self):
        return self.patrocinador


class RegulamentoDetalhe(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    urlvideo = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name_plural = '3.1) Regulamentos (Página)'

    def __str__(self):
        return self.titulo


class RegulamentoItem(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    pdf = models.FileField(upload_to='homepage/regulamentos/%Y/%m/%d/')
    img = models.ImageField(upload_to='homepage/regulamentos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name_plural = '3.2) Regulamentos (Itens)'

    def __str__(self):
        return self.titulo


class InscricaoDetalhe(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    urlvideo = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name_plural = '4.1) Inscrições (Página)'

    def __str__(self):
        return self.titulo


class InscricaoItem(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    link = models.CharField(max_length=250)
    img = models.ImageField(upload_to='homepage/inscricao/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name_plural = '4.2) Inscrições (Itens)'

    def __str__(self):
        return self.titulo


class Eventos(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    linkvideo = models.CharField(max_length=250)
    titulo = models.CharField(max_length=65)
    datainicio = models.DateTimeField(auto_now_add=False)
    datafim = models.DateTimeField(auto_now_add=False)
    resultado_pdf = models.FileField(upload_to='homepage/resultado/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '2.1) Eventos'

    def __str__(self):
        return self.titulo


class KendaExperience(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '6.1) Kenda Experience (Página)'

    def __str__(self):
        return self.titulo


class KendaExperienceCard(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    img = models.ImageField(upload_to='homepage/kendaexperiencecard/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '6.2) Kenda Experience Card'

    def __str__(self):
        return self.titulo


class KendaExperienceFotos(models.Model):
    titulo = models.CharField(max_length=65)
    img = models.ImageField(
        upload_to='homepage/kendaexperiencefotos/%Y/%m/%d/')
    kendaexperiencecard = models.ForeignKey(
        KendaExperienceCard, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '6.3) Kenda Experience Fotos'

    def __str__(self):
        return self.titulo


class Galeria(models.Model):
    titulo = models.CharField(max_length=65)
    img = models.ImageField(upload_to='homepage/galeria/%Y/%m/%d/')
    evento = models.ForeignKey(Eventos, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '2.2) Galeria de Imagens'

    def __str__(self):
        return self.titulo


class DataEvento(models.Model):
    titulo = models.CharField(max_length=65)
    data = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = '1.3) Data do Contador'

    def __str__(self):
        return self.titulo


class Sobre(models.Model):
    titulo = models.CharField(max_length=65)
    card1 = models.CharField(max_length=200)
    card2 = models.CharField(max_length=200)
    card3 = models.CharField(max_length=200)
    descricao = models.TextField()
    urlvideo = models.TextField()
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '1.1) Sobre (Página)'

    def __str__(self):
        return self.titulo


class Contato(models.Model):
    nome = models.CharField(max_length=120)
    phone = models.CharField(max_length=17)
    email = models.EmailField(max_length=254)
    assunto = models.CharField(max_length=120)
    message = models.TextField()
    lido = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '5.1) Contatos'

    def __str__(self):
        return self.assunto


class ESG(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '7.1) E.S.G. (Página)'

    def __str__(self):
        return self.titulo


class ESGCard(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    img = models.ImageField(upload_to='homepage/esgcard/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '7.2) E.S.G. Card'

    def __str__(self):
        return self.titulo


class ESGFotos(models.Model):
    titulo = models.CharField(max_length=65)
    img = models.ImageField(
        upload_to='homepage/esgfotos/%Y/%m/%d/')
    esgcard = models.ForeignKey(
        ESGCard, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '7.3) E.S.G. Fotos'

    def __str__(self):
        return self.titulo


class Midia(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '8.1) Midia (Página)'

    def __str__(self):
        return self.titulo


class MidiaCard(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.TextField()
    img = models.ImageField(upload_to='homepage/midiacard/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '8.2) Mídia Card'

    def __str__(self):
        return self.titulo


class MidiaFotos(models.Model):
    titulo = models.CharField(max_length=65)
    img = models.ImageField(
        upload_to='homepage/Midiafotos/%Y/%m/%d/')
    midiacard = models.ForeignKey(
        MidiaCard, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '8.3) Mídia Fotos'

    def __str__(self):
        return self.titulo
