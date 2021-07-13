from rest_framework import serializers

from boards.models import Board


class BoardSerializer(serializers.ModelSerializer):
    pass
    # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Board
        fields = "__all__"
