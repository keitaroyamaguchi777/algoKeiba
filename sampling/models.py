from django.db import models


class Uma_kihon(models.Model):
    """馬基本テーブル"""
    race_key = models.IntegerField('レースキー')
    blad_int = models.IntegerField('血統登録番号')
    age      = models.IntegerField('馬年齢')
    sex      = models.IntegerField('性別')
    class Meta:
        unique_together=(("race_key","blad_int"))


class Zensou(models.Model):
    """前走テーブル"""
    seiseki_key   = models.IntegerField('競争成績キー', primary_key=True)
    zensou_kyori  = models.IntegerField('前走距離')
    zensou_tm_sa  = models.IntegerField('前走タイム差')
    zensou_3ftm_before = models.IntegerField('前走前3Fタイム')
    zensou_3ftm_after  = models.IntegerField('前走後3Fタイム')


class Kyousouba(models.Model):
    """競走馬テーブル"""
    race_key = models.IntegerField('レースキー')
    blad_int = models.IntegerField('血統登録番号')
    umaban   = models.IntegerField('馬番')
    zensou_seiseki_key = models.IntegerField('前走競争成績キー')
    zensou_race_key    = models.IntegerField('前走レースキー')
    kyakushitu         = models.IntegerField('脚質')

    class Meta:
        unique_together=(("race_key","umaban"))


class Kishu_Sabun(models.Model):
    """騎手差分テーブル"""
    kisyu_code = models.IntegerField('騎手コード', blank=False)
    kisyu_mei  = models.CharField('騎手名', max_length=8, blank=True)
    kisyu_fukusyou = models.DecimalField('騎手複勝率', max_digits=10, decimal_places=9)

    def __str__(self):
        return self.kisyuMei


class Tyokuzen(models.Model):
    """直前情報テーブル"""
    race_key  = models.IntegerField('レースキー')
    umaban    = models.IntegerField('馬番')
    kinryou   = models.IntegerField('斤量')
    bataijyu  = models.IntegerField('馬体重')
    taijyu_zougen = models.IntegerField('体重増減')

    class Meta:
        unique_together=(("race_key","umaban"))


class Bangumi(models.Model):
    """番組テーブル"""
    race_key  = models.IntegerField('レースキー', primary_key=True)
    syussou_tousuu    = models.IntegerField('出走頭数')
    syoukin   = models.IntegerField('1着賞金')
