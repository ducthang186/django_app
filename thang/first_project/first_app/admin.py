from django.contrib import admin
from first_app.models import User1,Topic,AccessRecord,Webpage,MyForm 
# Register your models here.
admin.site.register(Topic)

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(User1)
# admin.site.register(MyForm)

class MyFormAdmin(admin.ModelAdmin):
    list_display =("name","email","text")
    search_fields =("name","email","text")
    list_display_links = ('name',)
    list_editable = ("email",)
admin.site.register(MyForm,MyFormAdmin)

# admin.site.register(UserProfileInfo)
