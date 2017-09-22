from django.db import models


class Uma_kihon(models.Model):
    """馬基本テーブル"""
    history = models.CharField('作成年月日', max_length=8, default='00000000')
    blad_int = models.IntegerField('血統登録番号', default=0)
    name     = models.CharField('馬名', max_length=54, blank=True)
    birthday = models.DateTimeField('生年月日')
    sex      = models.IntegerField('性別')
    class Meta:
        unique_together=(("history","blad_int"))

class Zensou(models.Model):
    """前走テーブル"""
    history = models.CharField('作成年月日', max_length=8, default='00000000')
    seiseki_key   = models.CharField('競争成績キー',
                        max_length=16, primary_key=True)
    zensou_kyori  = models.IntegerField('前走距離')
    zensou_tm_sa  = models.DecimalField('前走タイム差', max_digits=4, decimal_places=2)
    zensou_3ftm_before = models.DecimalField('前走前3Fタイム', max_digits=4, decimal_places=2)
    zensou_3ftm_after  = models.DecimalField('前走後3Fタイム', max_digits=4, decimal_places=2)

class Kyousouba(models.Model):
    """競走馬テーブル"""
    history = models.CharField('作成年月日', max_length=8, default='00000000')
    race_key = models.IntegerField('レースキー')
    umaban   = models.IntegerField('馬番')
    blad_int = models.IntegerField('血統登録番号')
    kyakushitu         = models.IntegerField('脚質')
    zensou_seiseki_key = models.CharField('前走競争成績キー', max_length=16, blank=True)
    zensou_race_key    = models.CharField('前走レースキー', max_length=8, blank=True)
    class Meta:
        unique_together=(("history","race_key","umaban"))


class Kyousouba_Extend(models.Model):
    """競走馬拡張テーブル"""
    history = models.CharField('作成年月日', max_length=8, default='00000000')
    race_key = models.IntegerField('レースキー')
    umaban   = models.IntegerField('馬番')
    jra_seiseki_1chaku = models.IntegerField('JRA成績1着')
    jra_seiseki_2chaku = models.IntegerField('JRA成績2着')
    jra_seiseki_3chaku = models.IntegerField('JRA成績3着')
    jra_seiseki_chakugai = models.IntegerField('JRA成績着外')
    class Meta:
        unique_together=(("history","race_key","umaban"))


class Kishu_Sabun(models.Model):
    """騎手差分テーブル"""
    history = models.CharField('作成年月日', max_length=8, default='00000000')
    kishu_code = models.IntegerField('騎手コード', blank=False)
    kishu_mei  = models.CharField('騎手名', max_length=8, blank=True)
    kishu_fukusyou = models.DecimalField('騎手複勝率', max_digits=10, decimal_places=9)
    class Meta:
        unique_together=(("history","kishu_code"))

class Chokuzen(models.Model):
    """直前情報テーブル"""
    history = models.CharField('作成年月日', max_length=8, default='00000000')
    race_key  = models.IntegerField('レースキー')
    umaban    = models.IntegerField('馬番')
    kishu_code = models.CharField('騎手コード', max_length=5, blank=True)
    kinryou   = models.DecimalField('斤量', max_digits=3, decimal_places=1)
    bataijyu  = models.CharField('馬体重', max_length=3, blank=True)
    taijyu_zougen = models.CharField('体重増減', max_length=3, blank=True)
    class Meta:
        unique_together=(("history","race_key","umaban"))


class Bangumi(models.Model):
    """番組テーブル"""
    history = models.CharField('作成年月日', max_length=8, default='00000000')
    race_key  = models.IntegerField('レースキー', primary_key=True)
    syussou_tousuu    = models.IntegerField('出走頭数')
    syoukin   = models.IntegerField('1着賞金')
    class Meta:
        unique_together=(("history","race_key"))
