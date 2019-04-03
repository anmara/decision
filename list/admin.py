from django.contrib import admin
from django.contrib.auth.models import Group
admin.site.unregister(Group)


admin.site.site_header = "iHire@CSPC"
admin.site.site_title = "iHire"
admin.site.site_index = "iHire administration"

# class InLineEduc_Qua1(admin.StackedInline):
#    model = Educ_Qua21
#    max_num = 1
#
#
# class InLineEduc_Qua2(admin.StackedInline):
#    model = Educ_Qua2
#    max_num = 1
#
#
# class InLineEduc_Qua21(admin.StackedInline):
#    model = Educ_Qua21
#    max_num = 1
#
#
# class InLineProf_Dev(admin.StackedInline):
#    model = Prof_Dev
#   max_num = 1
#
#
# class InLineProf_Dev1(admin.StackedInline):
#    model = Prof_Dev1
#    max_num = 1
#
#
# class InLineProf_Dev2(admin.StackedInline):
#    model = Prof_Dev2
#    max_num = 1
#
#
# class InLineProf_Devb(admin.StackedInline):
#    model = Prof_Devb
#    max_num = 1
#
#
# class InLineProf_Devc(admin.StackedInline):
#    model = Prof_Devc
#    max_num = 1
#
#
# class InLineProf_Devd(admin.StackedInline):
#    model = Prof_Devd
#    max_num = 1
#
#
# admin.register(Educ_Qua1)
#
#
# class InLineProf_Deve(admin.StackedInline):
#   model = Prof_Deve
#   max_num = 1
#
#
# class InLineProf_Devf(admin.StackedInline):
#   model = Prof_Devf
#   max_num = 1


# class ApplicantAdmin(admin.ModelAdmin):
#    inlines = [InLineEduc_Qua1, InLineEduc_Qua2, InLineEduc_Qua21, InLineProf_Dev, InLineProf_Dev1, InLineProf_Dev2, InLineProf_Devb, InLineProf_Devc, InLineProf_Devd, InLineProf_Deve, InLineProf_Devf]
#    list_display = ('name', 'area_of_specialization', 'date_recorded', 'user')
#    list_display_links = ('name', 'area_of_specialization', 'date_recorded', 'user')
#    list_filter = ('area_of_specialization', 'user', 'date_recorded')
#    fieldsets = (
#        (None, {
#            'fields': (
#                'fname',
#                'mname',
#                'lname',
#                'area_of_specialization',
#                'user'
#            )
#        }),
#    )
#
#    def name(self, obj):
#        return "{} {} {}".format(obj.fname, obj.mname, obj.lname)
#
#
#admin.site.register(Applicant, ApplicantAdmin)
