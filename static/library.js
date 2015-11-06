"use strict";

function loadSongs() {
	var songreq = new XMLHttpRequest();
	songreq.onreadystatechange = function(e) {
		if (songreq.readyState == XMLHttpRequest.DONE) {
			var text = songreq.responseText;
			if (text) {
				addSongs(JSON.parse(text));
			} else {
				alert("An error occurred loading the song database");
			}
		}
	};
	songreq.open("GET", "/library_json/");
	songreq.send();
}

function addSongs(songs) {
	var table = document.getElementById("lib-table");
	var tbody = table.getElementsByTagName("tbody")[0];
	for (var si in songs) {
		var song = songs[si];
		console.log(tbody);
		var row = document.createElement("tr");
			var titledata = document.createElement("td");
				titledata.innerHTML = song.title;
			row.appendChild(titledata);
			var urldata = document.createElement("td");
				urldata.innerHTML = song.url;
			row.appendChild(urldata);
		
		tbody.appendChild(row);
	}
	//console.log(songs);
}