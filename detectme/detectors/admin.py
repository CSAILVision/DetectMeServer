from django.contrib import admin
from .models import Detector, AnnotatedImage


class DetectorAdmin(admin.ModelAdmin):
    readonly_fields = ('hash_value', )

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.
        """
        if not change:
            if not obj.author:
                obj.author = request.user.get_profile()
        obj.save()


class AnnotatedImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_width', 'image_height', )


admin.site.register(Detector, DetectorAdmin)
admin.site.register(AnnotatedImage, AnnotatedImageAdmin)

