from django.contrib import admin
from .models import Detector, AnnotatedImage, Rating, ExtraInfo, Performance


class DetectorAdmin(admin.ModelAdmin):
    readonly_fields = ('hash_value', 'average_rating', 'number_ratings')
    list_filter = ('is_deleted', 'is_public')

    def average_rating(self, instance):
        return instance.average_rating

    def number_ratings(self, instance):
        return instance.number_ratings

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.
        """
        if not change:
            if not obj.author:
                obj.author = request.user.get_profile()
        obj.save()


class AnnotatedImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_width', 'image_height', )


class RatingAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.
        """
        if not change:
            if not obj.author:
                obj.author = request.user.get_profile()
        obj.save()


admin.site.register(Detector, DetectorAdmin)
admin.site.register(AnnotatedImage, AnnotatedImageAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(ExtraInfo)
admin.site.register(Performance)
