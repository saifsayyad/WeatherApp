import os

from groundwork_web.patterns import GwWebPattern
from groundwork.patterns import GwCommandsPattern
from weatherapp.patterns.YahooApiPattern.YahooApiPattern import YahooApiPattern, YahooApiException


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
        try:
            YahooApiPattern.set_query_params(self, location='jalgaon', u='f')
            response = YahooApiPattern.get_weathter_info(self)
        except Exception as e:
            self.log.error(str(e))
            self.log.info("Retrying!!")

            try:
                YahooApiPattern.refresh_time_stamp(self)
                YahooApiPattern.refresh_oauth_nonce(self)
                response = YahooApiPattern.get_weathter_info(self)
            except Exception as e:
                self.log.error(str(e))
                response = str(e)

        return response
