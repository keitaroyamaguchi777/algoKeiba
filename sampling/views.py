from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from sampling.models import Uma_kihon
from sampling.models import Bangumi
from sampling.models import Tyokuzen
from sampling.models import Zensou
from sampling.models import Kishu_Sabun
from sampling.models import Kyousouba
from sampling.forms import UmaKihonForm

def uma_kihon_list(request):
    """馬基本情報の一覧"""
    umaKihon = Uma_kihon.objects.all().order_by('blad_int')
    return render(request,
                  'sampling/uma_kihon_list.html',
                  {'uma_kihon': umaKihon})

def uma_kihon_edit(request, blad_int=None):
    """馬基本情報の編集"""
    if blad_int:   # id 指定 (修正時)
        umaKihon = get_object_or_404(Uma_kihon, pk=blad_int)
    else:         # (追加時)
        umaKihon = Uma_kihon()

    if request.method == 'POST':
        # POST された request データからフォームを作成
        form = UmaKihonForm(request.POST, instance=umaKihon)

        if form.is_valid():
            umaKihon = form.save(commit=False)
            umaKihon.save()
            return redirect('sampling:uma_kihon_list')
    else:    # GET の時
        form = UmaKihonForm(instance=umaKihon)

    return render(request, 'sampling/uma_kihon_edit.html',
            dict(form=form, blad_int=blad_int))

def uma_kihon_del(request, blad_int):
    """馬基本情報の削除"""
    umaKihon = get_object_or_404(Uma_kihon, pk=blad_int)
    umaKihon.delete()
    return redirect('sampling:uma_kihon_list')

def bangumi_list(request):
    """番組情報の一覧"""
    bangumi = Bangumi.objects.all().order_by('race_key')
    return render(request,
                  'sampling/bangumi_list.html',
                  {'bangumi': bangumi})

def tyokuzen_list(request):
    """直前情報の一覧"""
    tyokuzen = Tyokuzen.objects.all().order_by('id')
    return render(request,
                  'sampling/tyokuzen_list.html',
                  {'tyokuzen': tyokuzen})

def zensou_list(request):
    """前走情報の一覧"""
    zensou = Zensou.objects.all().order_by('seiseki_key')
    return render(request,
                  'sampling/zensou_list.html',
                  {'zensou': zensou})

def kishu_sabun_list(request):
    """騎手情報の一覧"""
    kishu_sabun = Kishu_Sabun.objects.all().order_by('id')
    return render(request,
                  'sampling/kishu_sabun_list.html',
                  {'kishu_sabun': kishu_sabun})

def kyousouba_list(request):
    """騎手情報の一覧"""
    kyousouba = Kyousouba.objects.all().order_by('id')
    return render(request,
                  'sampling/kyousouba_list.html',
                  {'kyousouba': kyousouba})
