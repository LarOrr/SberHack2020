function showChart(endpoint, start_date, end_date, chart_type) {
     // alert("Hello World")
     var query = '?start_date=' + start_date + '&end_date=' + end_date;
    fetch ('/'+endpoint+query)
		.then (
			function (response) {
				if (response.status === 200) {
					response.json().then(function (counts) {
						var txt = '<img src="';
						txt += createChartLink(counts, chart_type);
						txt += '">';
						// Adds chart image to the page
                        //  alert(txt);
						document.getElementById("resultChart").innerHTML = txt
					});
				} else {
					alert ("Error: " + response.status);
				}
			}
		);
}

function createChartLink(counts, chart_type) {
     // TODO fix link - chart looks bad :/
     var link = "https://quickchart.io/chart?c={type:'" + chart_type + "',data:";
     var keys = [];
     var values = [];
     for (var key in counts) {
          keys.push(key);
          values.push(counts[key]);
     }
     link += "{labels:" + JSON.stringify(keys) + ", datasets:[{data:" + JSON.stringify(values) + "}]}}";
     // TODO fix or make link to image
     // Otherwise incorrect HTML insertion
     return link.replace(/"/g, "'");
}