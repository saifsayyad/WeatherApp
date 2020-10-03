def test_import_weatherapp():
    import weatherapp
    assert weatherapp is not None


def test_weatherapp_plugin_activation():
    from weatherapp.applications import WEATHERAPP_APP
    from weatherapp.plugins import weatherapp_plugin

    my_app = WEATHERAPP_APP()
    app = my_app.app
    app.plugins.activate(["weatherapp_plugin"])
    plugin = app.plugins.get("weatherapp_plugin")
    assert plugin is not None
    assert isinstance(plugin, weatherapp_plugin)
