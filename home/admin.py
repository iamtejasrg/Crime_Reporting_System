from django.contrib import admin
from home.models import Contact,Signup, Login,Complaint
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'uname', 'psw')

class SignupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname','phone', 'email','add','file', 'pwd','rpwd')
    list_display_links =('id','name','surname')
    search_fields=('name','surname')

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ( 'id','name', 'place','Description', 'PhysicalEvidence','fileUpload')
    list_display_links =('id','name','place')
    search_fields=('id','name')



# Register your models here.
admin.site.register(Contact)
admin.site.register(Signup,SignupAdmin)
admin.site.register(Login,LoginAdmin)
admin.site.register(Complaint,ComplaintAdmin)