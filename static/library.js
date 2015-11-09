"use strict";

var SORT_TITLE_ASC = 1;
var SORT_TITLE_DEC = 2;
var SORT_ARTIST_ASC = 3;
var SORT_ARTIST_DEC = 4;

var sortmode = 0;

function bullshit() {
	var len = Math.floor(Math.random()*20)+5;
	var shits = "qwertyuiopasdfghjklzxcvbnm1234567890._";
	var s = "";
	for (var i = 0; i < len; i++) {
		var l = shits.charAt(Math.floor(Math.random()*shits.length));
		s += l;
	}
	return s;
}

function make_testjson() {
	var test = [];
	for (var i = 0; i < 20; i++) {
		var tests = {};
		tests.title = bullshit();
		tests.url = bullshit();
		test.push(tests);
	}
	console.log(JSON.stringify(test));
}

function toggleSortTitle() {return toggleSort(true);}
function toggleSortArtist() {return toggleSort(false);}

function toggleSort(title) {
	var tca = document.getElementById("titlesort-chev-up"); tca.style.display = "none";
	var tcd = document.getElementById("titlesort-chev-down"); tcd.style.display = "none";
	var aca = document.getElementById("artistsort-chev-up"); aca.style.display = "none";
	var acd = document.getElementById("artistsort-chev-down"); acd.style.display = "none";
	
	if (title) {
		if (sortmode == SORT_TITLE_ASC) {
			sortmode = SORT_TITLE_DEC;
			tcd.style.display = "";
		} else {
			sortmode = SORT_TITLE_ASC;
			tca.style.display = "";
		}
	} else {
		if (sortmode == SORT_ARTIST_ASC) {
			sortmode = SORT_ARTIST_DEC;
			acd.style.display = "";
		} else {
			sortmode = SORT_ARTIST_ASC;
			aca.style.display = "";
		}
	}
	
	updateSort();
}

function updateSort() {
	var tbody = document.getElementById("lib-table").getElementsByTagName("tbody")[0];
	var col, asc;
	switch (sortmode) {
		case SORT_TITLE_ASC:
			col = 0;
			asc = 1;
			break;
		case SORT_TITLE_DEC:
			col = 0;
			asc = -1;
			break;
		case SORT_ARTIST_ASC:
			col = 1;
			asc = 1;
			break;
		case SORT_ARTIST_DEC:
			col = 1;
			asc = -1;
			break;
		default: return;
	}
	
	var rows = tbody.rows, rlen = rows.length, arr = new Array(), i, j, cells, clen;
	// fill the array with values from the table
	for(i = 0; i < rlen; i++){
	cells = rows[i].cells;
	clen = cells.length;
	arr[i] = new Array();
		for(j = 0; j < clen; j++){
			arr[i][j] = cells[j].innerHTML;
		}
	}
	// sort the array by the specified column number (col) and order (asc)
	arr.sort(function(a, b){
		return (a[col] == b[col]) ? 0 : ((a[col] > b[col]) ? asc : -1*asc);
	});
	for(i = 0; i < rlen; i++){
		arr[i] = "<td>"+arr[i].join("</td><td>")+"</td>";
	}
	tbody.innerHTML = "<tr>"+arr.join("</tr><tr>")+"</tr>";
}

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

function doSearch() {
	var searchfield = document.getElementById("lib-search-field");
	var searchtext = searchfield.value;
	var tbody = document.getElementById("lib-table").getElementsByTagName("tbody")[0];
	
	for (var r = 0; r < tbody.rows.length; r++) {
		var found = false;
		var row = tbody.rows[r];
		for (var c = 0; c < row.children.length; c++) {
			//console.log(row.children[c]);
			var text = row.children[c].innerHTML;
			if (text.toUpperCase().indexOf(searchtext.toUpperCase()) != -1) {
				found = true;
				break;
			}
		}
		if (found) {
			row.style.display = "";
		} else {
			row.style.display = "none";
		}
	}
}

function addSongs(songs) {
	var table = document.getElementById("lib-table");
	var tbody = table.getElementsByTagName("tbody")[0];
	for (var si in songs) {
		var song = songs[si];
		//console.log(tbody);
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