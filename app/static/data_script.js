console.log("Fuck You")

function displayFuck() {
	console.log("FUCKKKK")
}

async function getCurrentWeather() {
	let url = 'http://api.weatherapi.com/v1/current.json?key=bbcdbab400484c019e182748221707&q=Bengaluru&aqi=no';
	let response = await fetch(url);
	if (response.status != 200) {
		$("#current_real_temp").html("NA");
	}
	let data = await response.json();
	$("#current_real_temp").html(data.current.temp_c + " &degC");
}

async function getBoltTemp() {
	let url = '/get_bolt_temp';
	let response = await fetch(url);
	if (response.status != 200) {
		$("#current_bolt_temp").html("NA");
	}
	let data = await response.json();
	$("#current_bolt_temp").html(data.data + " &degC");
}

async function getBoltRain() {
	let url = '/get_rain_status';
	let response = await fetch(url);
	if (response.status != 200) {
		$("#current_rain_status").html("NA");
	}
	let data = await response.json();
	if (data.data == "Not Raining") {
		$("#current_rain_status").css("font-size", "60px");
		$("#current_rain_status").html(data.data);
	}
	else {
		$("#current_rain_status").css("font-size", "70px");
		$("#current_rain_status").html(data.data);
	}
}

setInterval(getCurrentWeather, 10000);
setInterval(getBoltTemp, 10000);
setInterval(getBoltRain, 10000);