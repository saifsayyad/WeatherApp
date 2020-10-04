      google.charts.load('current', {'packages':['line', 'corechart']});
      google.charts.setOnLoadCallback(drawChart);
    function drawChart() {

      var weekday = new Array(7);
      weekday[0] = "Sunday";
      weekday[1] = "Monday";
      weekday[2] = "Tuesday";
      weekday[3] = "Wednesday";
      weekday[4] = "Thursday";
      weekday[5] = "Friday";
      weekday[6] = "Saturday";

      var button = document.getElementById('change-chart');
      var chartDiv = document.getElementById('chart_div');

      var data = new google.visualization.DataTable();
      data.addColumn('date', 'Month');
      data.addColumn('number', "Average Temperature");
      data.addColumn('number', "Average Hours of Daylight");
      allData = [['Day', 'Min temp', 'Max temp']];
      allDates = [];
      console.log(weatherData);
      city = weatherData.location.city;
      country = weatherData.location.country;

      for (var k in weatherData.forecasts){

        low_temp = weatherData.forecasts[k].low;
        high_temp = weatherData.forecasts[k].high;
        date = new Date(0);
        date.setUTCSeconds(Math.floor(weatherData.forecasts[k].date));
        day = weatherData.forecasts[k].day;
        allData.push([day, low_temp, high_temp]);
        if (allDates.length === 0){
            allDates.push(date);
        }
      }
      allDates.push(date);

     var dateOptions = { year: 'numeric', month: 'long', day: 'numeric' };
     var from  = allDates[0].toLocaleDateString("en-US", dateOptions);
     var toDate = allDates[1].toLocaleDateString("en-US", dateOptions);

      var data = google.visualization.arrayToDataTable(allData);

        var options = {
          title: city + ', ' + country,
          height: 600,
          width: 1000,
          hAxis: {title: from + '- ' + toDate,  titleTextStyle: {color: '#333'}},
          vAxis: {title: 'Temp', minValue: 0}
        };

        var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      weatherData = null;
    }