from django.core.exceptions import ValidationError

def validate_title_content(value):
    if "#" in value:
        raise ValidationError('#은 들어갈 수 없어요.')
