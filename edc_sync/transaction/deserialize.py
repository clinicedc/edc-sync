from django.core import serializers


def deserialize(json_text=None):
    """Returns a generator of deserialized objects.

    Wraps django deserialize with defaults for JSON
    and natural keys.
    """
    return serializers.deserialize(
        "json", json_text,
        ensure_ascii=True,
        use_natural_foreign_keys=True,
        use_natural_primary_keys=False)
