from django.contrib import admin
from .models import Detector, Annotation, AnnotatedImage, Performance


class DetectorAdmin(admin.ModelAdmin):
    readonly_fields = ('object_class', 'user', )

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.
        """
        if not change:
            obj.user = request.user.get_profile()
        obj.save()


class AnnotatedImageAdmin(admin.ModelAdmin):
    readonly_fields = ('width', 'height', )


admin.site.register(Detector, DetectorAdmin)
admin.site.register(Annotation)
admin.site.register(AnnotatedImage, AnnotatedImageAdmin)
admin.site.register(Performance)
