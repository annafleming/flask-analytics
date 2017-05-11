from .settings import column_scale


def change_column_scale(column):
    if column.name not in column_scale:
        raise Exception('Scale settings are missing for the column %s' % column.name)

    settings = column_scale[column.name]

    if 'Default' not in settings:
        raise Exception('Default value is missing in settings')
    return column.apply(lambda x: settings[x] if x in settings else settings['Default'])
