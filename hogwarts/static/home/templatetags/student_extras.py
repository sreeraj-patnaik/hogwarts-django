from django import template

register = template.Library()

@register.filter
def get_sgpa(student, sem):
    """
    Returns the SGPA of a given student for semester `sem`.
    Example: student|get_sgpa:3
    """
    return getattr(student, f"sgpa_sem{sem}", None)
