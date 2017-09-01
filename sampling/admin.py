from django.contrib import admin
from sampling.models import Uma_kihon,Zensou,Kyousouba,Kishu_Sabun,Tyokuzen,Bangumi

# Register your models here.


class UmaKihonAdmin(admin.ModelAdmin):
    list_display = ('id', 'race_key', 'blad_int', 'age', 'sex',)
    list_display_links = ('id',)
admin.site.register(Uma_kihon, UmaKihonAdmin)


class ZensouAdmin(admin.ModelAdmin):
    list_display = ('seiseki_key', 'zensou_kyori', 'zensou_tm_sa',
            'zensou_3ftm_before', 'zensou_3ftm_after',)
    list_display_links = ('seiseki_key',)
admin.site.register(Zensou, ZensouAdmin)


class KyousoubaAdmin(admin.ModelAdmin):
    list_display = ('race_key', 'blad_int', 'umaban',
            'zensou_seiseki_key', 'zensou_race_key', 'kyakushitu',)
    list_display_links = ('race_key',)
admin.site.register(Kyousouba, KyousoubaAdmin)


class KishuSabunAdmin(admin.ModelAdmin):
    list_display = ('kisyu_code', 'kisyu_fukusyou', 'kisyu_mei',)
    list_display_links = ('kisyu_code',)
admin.site.register(Kishu_Sabun, KishuSabunAdmin)


class TyokuzenAdmin(admin.ModelAdmin):
    list_display = ('race_key', 'umaban', 'kinryou',
            'bataijyu', 'taijyu_zougen',)
    list_display_links = ('race_key',)
admin.site.register(Tyokuzen, TyokuzenAdmin)


class BangumiAdmin(admin.ModelAdmin):
    list_display = ('race_key', 'syussou_tousuu', 'syoukin',)
    list_display_links = ('race_key',)
admin.site.register(Bangumi, BangumiAdmin)
