from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def timesince_first(value):
    """Return only the first time unit from timesince output, with abbreviated units."""
    time_str = timesince(value)
    first_unit = time_str.split(",")[0].strip()  # Get the first unit and remove extra spaces
    
    # Define abbreviations for each unit
    abbreviations = {
        "minutes": "m",
        "minute": "m",
        "hours": "h",
        "hour": "h",
        "days": "d",
        "day": "d",
        "weeks": "w",
        "week": "w",
        "months": "mo",
        "month": "mo",
        "years": "y",
        "year": "y",
    }
    
    # Replace the unit in the string with the abbreviation
    for word, abbrev in abbreviations.items():
        if word in first_unit:
            # Remove space between number and abbreviation
            number_part = first_unit.split()[0]  # Get the number part
            return number_part + abbrev  # Concatenate without space
    
    return first_unit  # Fallback in case no match is found
