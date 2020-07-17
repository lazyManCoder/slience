from rest_framework import serializers
from apps.user.models import Show,Comment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment        # 与Book表对应
        fields = "__all__"

