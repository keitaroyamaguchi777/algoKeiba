from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from sampling.models import Uma_kihon
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
