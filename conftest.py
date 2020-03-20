from pytest_djangoapp import configure_djangoapp_plugin

gettext = lambda s: s

pytest_plugins = configure_djangoapp_plugin(
    {
        'LANGUAGES': (
            ('en', gettext('English')),
            ('de', gettext('German')),
            ('fr', gettext('French')),
            ('it', gettext('Italian')),
            ('es', gettext('Spanish')),
        ),
    },
    extend_INSTALLED_APPS=[
        'modeltranslation',
    ]
)
