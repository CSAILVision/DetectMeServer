from rest_framework import serializers
from .models import Box


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ('id','detector','xcoord','ycoord','created')


    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.detector = attrs.get('detector', instance.detector)
            instance.xcoord = attrs.get('xcoord', instance.xcoord)
            instance.ycoord = attrs.get('ycoord', instance.ycoord)
            instance.created = attrs.get('created', instance.created)
            return instance

        # Create new instance
        return Box(**attrs)