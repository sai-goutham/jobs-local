from django.contrib import admin
from testap.models import hydjobs,punejobs,bangjobs,ndljobs
# Register your models here.
class hydjobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneNumber']

class punejobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneNumber']

class bangjobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneNumber']

class ndljobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneNumber']


admin.site.register(hydjobs,hydjobAdmin)
admin.site.register(punejobs,punejobAdmin)
admin.site.register(bangjobs,bangjobAdmin)
admin.site.register(ndljobs,ndljobAdmin)
