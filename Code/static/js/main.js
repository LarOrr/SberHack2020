function showChart(endpoint, start_date, end_date, chart_type) {
     // alert("Hello World")
	// changeInnerHtml("")
	document.getElementById("resultChart").textContent = "Loading chart...";
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
     // TODO fix link - chart looks bad sometimes :/
     var link = "https://quickchart.io/chart?c={type:'" + chart_type + "',data:";
     var keys = [];
     var values = [];
     for (var key in counts) {
          keys.push(key);
          values.push(counts[key]);
     }
     link += "{labels:" + JSON.stringify(keys) + ", datasets:[{data:" + JSON.stringify(values) + "}]}";
     // link = "doughnutlabel:{" +
		//  "labels:[{" +
		//  "text:" + values.reduce((a, b) => a + b, 0) + "," +
		//  " font:{" +
		//  " size:20," +
		//  "weight:'bold'" +
		//  "}" +
		//  "},{" +
		//  "text:'total'" +
		//  "}]";
	 link += "}";
     // TODO make link to image?
     // Otherwise incorrect HTML insertion
     return link.replace(/"/g, "'");
}