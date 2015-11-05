"use strict"

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
	console.log(songs);
}