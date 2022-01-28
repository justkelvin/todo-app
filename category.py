def cat_color(category):
    """Add more categories to differentiate colors"""
    COLORS = {
        'Learn': 'Cyan',
        'YouTube': 'red',
        'Sports': 'cyan',
        'Study': 'green',
        'Entertainment': 'yellow'
    }
    if category in COLORS:
        return COLORS[category]
    return 'white'