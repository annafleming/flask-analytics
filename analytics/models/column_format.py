

def change_column_scale(column, settings):
    if 'Default' not in settings:
        raise Exception('Default value is missing in settings')
    return column.apply(lambda x: settings[x] if x in settings else settings['Default'])
