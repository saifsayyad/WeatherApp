# WeatherApp

This is a web application to fetch data from Yahoo Weather server and display forecast info.

## Setup steps

1. To create a virtual env please follow https://docs.python.org/3/library/venv.html this link.

2. Enter below command in cmd/terminal to checkout thit repository
    
    ``git clone https://github.com/saifsayyad/WeatherApp.git``

3. Start you virtual env
4. Then CD into the checkedout directory
5. Run `` pip install -r requirements.txt`` command to install the required dependancies
6. Then install weatherapp by runnint ``pip install -e .``
7. Run ``weatherapp server_start flask_debug`` to start a Flask server

## Usage

* After starting the ``flask`` server you can visit ``http://127.0.0.1:5000/check``
* This will show default weather status of ``Nasik`` city
* You can enter the parameters in the ``Search params`` window and press ``submit`` to see the result
* To know more about the parameters please refer https://developer.yahoo.com/weather/documentation.html#params this link.

## Note:

* Main development dirs are:
  * For flask implementation ``weatherapp/plugins/yahoo_api_plugin/yahoo_api_plugin.py``
  * For Yahoo weather api implementation ``weatherapp/patterns/YahooApiPattern/YahooApiPattern.py``

This application is developed using ``GroundWork`` microframework to know more visit https://groundwork.readthedocs.io/en/latest/
