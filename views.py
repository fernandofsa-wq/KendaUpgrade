
from urllib import request

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from .models import (ESG, Contato, DataEvento, ESGCard, ESGFotos, Eventos,
                     Galeria, InscricaoDetalhe, InscricaoItem, KendaExperience,
                     KendaExperienceCard, KendaExperienceFotos, Midia,
                     MidiaCard, MidiaFotos, Patrocinio, RegulamentoDetalhe,
                     RegulamentoItem, Sliders, Sobre, redessociais)


def contato(request):
    sobre = Sobre.objects.get(pk=2)
    sliders = Sliders.objects.filter(is_published=True).order_by('id')
    patrocinios = Patrocinio.objects.filter(is_published=True).order_by('id')
    evento = Eventos.objects.filter(is_published=True).order_by('id')

    if request.method == "POST":

        nome = request.POST.get('nome')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        message = request.POST.get('message')

        contato = Contato(nome=nome, phone=phone, email=email,
                          assunto=assunto, message=message)
        contato.save()

    return render(request, 'homepage/pages/index.html', {
        'sliders': sliders,
        'patrocinios': patrocinios,
        'evento': evento,
        'sobre': sobre,
        'nome': nome,

    })

    # enviar email


def home(request):
    sobre = Sobre.objects.get(pk=2)
    sliders = Sliders.objects.filter(is_published=True).order_by('id')
    patrocinios = Patrocinio.objects.filter(is_published=True).order_by('id')
    evento = Eventos.objects.filter(is_published=True).order_by('id')
    contato = redessociais.objects.filter(is_published=True).get(pk=1)
    facebook = redessociais.objects.filter(is_published=True).get(pk=2)
    instagram = redessociais.objects.filter(is_published=True).get(pk=3)
    twitter = redessociais.objects.filter(is_published=True).get(pk=4)
    tiktok = redessociais.objects.filter(is_published=True).get(pk=5)
    youtube = redessociais.objects.filter(is_published=True).get(pk=6)
    linkedin = redessociais.objects.filter(is_published=True).get(pk=7)
    pinterest = redessociais.objects.filter(is_published=True).get(pk=8)
    inscrever = redessociais.objects.filter(is_published=True).get(pk=9)

    return render(request, 'homepage/pages/index.html', context={
        'sliders': sliders,
        'patrocinios': patrocinios,
        'evento': evento,
        'sobre': sobre,
        'contato': contato,
        'facebook': facebook,
        'instagram': instagram,
        'twitter': twitter,
        'tiktok': tiktok,
        'youtube': youtube,
        'linkedin': linkedin,
        'pinterest': pinterest,
        'inscrever': inscrever,


    })


def slider(request):
    slider = Sliders

    return render(request, 'homepage/partials/sliderone.html', context={
        'slider': slider,
        'is_detail_page': True,
    })


def patrocinio(request):
    patrocinio = Patrocinio

    return render(request, 'homepage/partials/patrocinio.html', context={
        'patrocinio': patrocinio,
        'is_detail_page': True,

    })


def informacoes(request):
    sobre = Sobre.objects.get(pk=2)
    regulamentodetalhe = RegulamentoDetalhe.objects.get(pk=1)
    regulamentoitem = RegulamentoItem.objects.filter(
        is_published=True).order_by('id')
    evento = Eventos.objects.filter(is_published=True).order_by('id')

    return render(request, 'homepage/pages/regulamento.html', context={
        'regulamento': regulamentoitem,
        'evento': evento,
        'regulamentodetalhe': regulamentodetalhe,
        'sobre': sobre,

    })


def inscricao(request):
    inscricaodetalhe = InscricaoDetalhe.objects.get(pk=1)
    sobre = Sobre.objects.get(pk=2)
    evento = Eventos.objects.filter(is_published=True).order_by('id')
    inscricaoitens = InscricaoItem.objects.filter(
        is_published=True).order_by('id')

    return render(request, 'homepage/pages/inscricao.html', context={
        'evento': evento,
        'inscricaoitens': inscricaoitens,
        'inscricaodetalhe': inscricaodetalhe,
        'sobre': sobre,


    })


def eventos(request):
    sobre = Sobre.objects.get(pk=2)
    eventos = Eventos.objects.filter(is_published=True).order_by('id')

    return render(request, 'homepage/pages/eventosmobile.html', context={
        'eventos': eventos,
        'sobre': sobre,

    })


def ver_evento(request, id):
    sobre = Sobre.objects.get(pk=2)
    ver_evento = Eventos.objects.get(pk=id)
    evento = Eventos.objects.filter(is_published=True).order_by('id')
    id_evento = ver_evento
    foto = Galeria.objects.filter(
        evento=id_evento)

    return render(request, 'homepage/pages/evento.html', {
        'ver_evento': ver_evento,
        'evento': evento,
        'foto': foto,
        'sobre': sobre,

    })


class DataEventoJson(View):
    def get(self, *args, **kwargs):
        dataevento = list(DataEvento.objects.values())
        return JsonResponse({
            'dataevento': dataevento,
        }, safe=False)


def mensagens(request):

    contatos = Contato.objects.filter(lido=False).order_by('-id')

    return render(request, 'homepage/pages/mensagens.html', context={
        'contatos': contatos,


    })


def lido_mensagens(request, id):
    contato_id = Contato.objects.get(pk=id)
    ident = contato_id.id
    nome = contato_id.nome
    data = contato_id.data
    phone = contato_id.phone
    email = contato_id.email
    assunto = contato_id.assunto
    message = contato_id.message
    mudar_contato = Contato(id=ident, data=data, nome=nome, phone=phone,
                            email=email, assunto=assunto, message=message, lido=True)
    mudar_contato.save()

    return redirect('../../mensagens/343536')


def loginmsg(request):
    return render(request, 'homepage/pages/loginmensagens.html')


def acesso_mensagem(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        buscar_usuario = User.objects.get(username=usuario)
        buscar_senha = User.objects.get(password=senha)
        check_password(senha, buscar_usuario.password)
        # confirma_senha =

        return HttpResponse(buscar_senha)

        # if confirmar_senha == True:
        # return redirect('../../mensagens/343536')


def kendaexperience(request):
    kendaexperiencedetalhe = KendaExperience.objects.get(pk=1)
    sobre = Sobre.objects.get(pk=2)
    kendaexperiencecard = KendaExperienceCard.objects.filter(
        is_published=True).order_by('id')
    evento = Eventos.objects.filter(is_published=True).order_by('id')

    return render(request, 'homepage/pages/kendaexperience.html', context={
        'kendaexperiencedetalhe': kendaexperiencedetalhe,
        'sobre': sobre,
        'kendaexperiencecard': kendaexperiencecard,
        'evento': evento,


    })


def kendaexperiencefotos(request, id):
    sobre = Sobre.objects.get(pk=2)
    kendaexperiencecard = KendaExperienceCard.objects.get(pk=id)
    id_card = kendaexperiencecard
    galeria = KendaExperienceFotos.objects.filter(
        kendaexperiencecard=id_card)
    evento = Eventos.objects.filter(is_published=True).order_by('id')

    return render(request, 'homepage/pages/kendaexperiencedetalhe.html', {
        'kendaexperiencecard': kendaexperiencecard,
        'galeria': galeria,
        'sobre': sobre,
        'evento': evento,

    })


def esg(request):
    esgdetalhe = ESG.objects.get(pk=1)
    sobre = Sobre.objects.get(pk=2)
    esgcard = ESGCard.objects.filter(
        is_published=True).order_by('id')
    evento = Eventos.objects.filter(is_published=True).order_by('id')

    return render(request, 'homepage/pages/esg.html', context={
        'esgdetalhe': esgdetalhe,
        'sobre': sobre,
        'esgcard': esgcard,
        'evento': evento,


    })


def esgfotos(request, id):
    sobre = Sobre.objects.get(pk=2)
    esgcard = ESGCard.objects.get(pk=id)
    id_card = esgcard
    galeria = ESGFotos.objects.filter(
        esgcard=id_card)
    evento = Eventos.objects.filter(is_published=True).order_by('id')

    return render(request, 'homepage/pages/esgdetalhe.html', {
        'esgcard': esgcard,
        'galeria': galeria,
        'sobre': sobre,
        'evento': evento,

    })


def midia(request):
    midiadetalhe = Midia.objects.get(pk=1)
    sobre = Sobre.objects.get(pk=2)
    midiacard = MidiaCard.objects.filter(
        is_published=True).order_by('id')
    evento = Eventos.objects.filter(is_published=True).order_by('id')

    return render(request, 'homepage/pages/midia.html', context={
        'midiadetalhe': midiadetalhe,
        'sobre': sobre,
        'midiacard': midiacard,
        'evento': evento,


    })


def midiafotos(request, id):
    sobre = Sobre.objects.get(pk=2)
    midiacard = MidiaCard.objects.get(pk=id)
    id_card = midiacard
    galeria = MidiaFotos.objects.filter(
        midiacard=id_card)
    evento = Eventos.objects.filter(is_published=True).order_by('id')

    return render(request, 'homepage/pages/midiadetalhe.html', {
        'midiacard': midiacard,
        'galeria': galeria,
        'sobre': sobre,
        'evento': evento,

    })
