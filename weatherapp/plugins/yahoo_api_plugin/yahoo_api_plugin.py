import os

from groundwork_web.patterns import GwWebPattern
from groundwork.patterns import GwCommandsPattern
from weatherapp.patterns.YahooApiPattern.YahooApiPattern import YahooApiPattern, YahooApiException
from flask import request


class YahooApiPlugin(GwWebPattern, GwCommandsPattern, YahooApiPattern):

    def __init__(self, *args, **kwargs):
        self.name = self.__class__.__name__
        super().__init__(*args, **kwargs)

    def deactivate(self):
        pass

    def activate(self):
        static_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'yahoo_weather', 'static')
        template_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'yahoo_weather', 'templates')

        self.web.routes.register(url="/check", methods=["GET", "POST"], endpoint=self.__weather_view, name="Main Page",
                                 description="Landing page")

        self.web.contexts.register("weather",
                                   template_folder=template_folder,
                                   static_folder=static_folder,
                                   url_prefix="/weather",
                                   description="Context for Weather WUI")

    def __weather_view(self):
        # print(dir(request))
        # print(request.method)
        response = None
        if request.method == 'POST':
            query_args = {
                "u": request.form.get('unit', None),
                "location": request.form.get('loc', None),
                "woeid": request.form.get('woeid', None),
                "lat": request.form.get('lat', None),
                "lon": request.form.get('lon', None)
            }
            YahooApiPattern.set_query_params(self, **query_args)
        try:
            response = YahooApiPattern.get_weathter_info(self)
        except Exception as e:
            self.log.error(str(e))
            self.log.info("Retrying!!")

            try:
                response = YahooApiPattern.get_weathter_info(self)
            except Exception as e:
                self.log.error(str(e))
                response = str(e)

        return self.web.render("index.html", data=response)
