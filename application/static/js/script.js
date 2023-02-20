function current_datetime() {
	let today = new Date();
	const yyyy = today.getFullYear();
	const mm = String(today.getMonth() + 1).padStart(2, "0");
	const dd = String(today.getDate()).padStart(2, "0");
	const HH = String(today.getHours()).padStart(2, "0");
	const MM = today.getMinutes();
	let start_time = HH+":"+String(MM-5).padStart(2, "0")+":00";
	const end_time = HH+":"+String(MM).padStart(2, "0")+":00";
	if (MM-5 < 0) {
		/*if (parseInt(HH)-1 < 0) {
			start_time = HH+":"+String((MM-5)%60+60).padStart(2, "0")+":00";
		}*/
		start_time = String(parseInt(HH)-1).padStart(2, "0")+":"+String((MM-5)%60+60).padStart(2, "0")+":00";
		
		console.log(start_time)
	}

	today = yyyy+"-"+mm+"-"+dd;
	console.log(today);
	console.log(start_time);
	console.log(end_time);
	document.getElementById("date").defaultValue = today;
	document.getElementById("start_time").defaultValue = start_time;
	document.getElementById("end_time").defaultValue = end_time;
}


function toggle_transfer_type(id) {
	const div_now = document.getElementsByClassName("div_now")
	const div_automate = document.getElementsByClassName("div_automate")
	const div_daily = document.getElementsByClassName("div_daily");
	const div_weekly = document.getElementsByClassName("div_weekly");
	const div_monthly = document.getElementsByClassName("div_monthly");
	if (id=="transfer_type-0") {
		for (let i=0; i < div_now.length; i++) {
			div_now[i].style.visibility = "visible";
			div_now[i].style.display = "block";
		}
		for (let i=0; i < div_automate.length; i++) {
			div_automate[i].style.visibility = "hidden";
			div_automate[i].style.display = "none";
		}
		document.getElementById("div_btn").value = "Data Transfer";
	} else {
		for (let i=0; i < div_now.length; i++) {
			div_now[i].style.visibility = "hidden";
			div_now[i].style.display = "none";
		}
		for (let i=0; i < div_automate.length; i++) {
			div_automate[i].style.visibility = "visible";
			div_automate[i].style.display = "block";
		}
		div_daily[0].style.visibility = "hidden";
		div_daily[0].style.display = "none";
		div_weekly[0].style.visibility = "hidden";
		div_weekly[0].style.display = "none";
		div_monthly[0].style.visibility = "hidden";
		div_monthly[0].style.display = "none";
		document.getElementById("div_btn").value = "Schedule";
	}
}


function toggle_transfer_freq(id) {
	const div_daily = document.getElementsByClassName("div_daily");
	const div_weekly = document.getElementsByClassName("div_weekly");
	const div_monthly = document.getElementsByClassName("div_monthly");
	switch (id.substr(id.length-1)) {
		case "0":
			div_daily[0].style.visibility = "visible";
			div_daily[0].style.display = "block";
			div_weekly[0].style.visibility = "hidden";
			div_weekly[0].style.display = "none";
			div_monthly[0].style.visibility = "hidden";
			div_monthly[0].style.display = "none";
			break;
		case "1":
			div_daily[0].style.visibility = "hidden";
			div_daily[0].style.display = "none";
			div_weekly[0].style.visibility = "visible";
			div_weekly[0].style.display = "block";
			div_monthly[0].style.visibility = "hidden";
			div_monthly[0].style.display = "none";
			break;
		case "2":
			div_daily[0].style.visibility = "hidden";
			div_daily[0].style.display = "none";
			div_weekly[0].style.visibility = "hidden";
			div_weekly[0].style.display = "none";
			div_monthly[0].style.visibility = "visible";
			div_monthly[0].style.display = "block";
			break;
	}
}

/*function toggle_transfer_freq(id) {
	const freq_dur = document.getElementById("transfer_freq_dur");
	const freq_dur_span = document.getElementById("freq_dur_span");
	switch (id.substr(id.length-1)) {
		case "0":
			freq_dur.min = "1";
			freq_dur.max = "60";
			freq_dur_span.textContent = "Minute(s)";
			break;
		case "1":
			freq_dur.min = "1";
			freq_dur.max = "23";
			freq_dur_span.textContent = "Hour(s)";
			break;
		case "2":
			freq_dur.min = "1";
			freq_dur.max = "6";
			freq_dur_span.textContent = "Day(s)";
			break;
		case "3":
			freq_dur.min = "1";
			freq_dur.max = "4";
			freq_dur_span.textContent = "Week(s)";
			break;
		case "4":
			freq_dur.min = "1";
			freq_dur.max = "11";
			freq_dur_span.textContent = "Month(s)";
			break;
	}
}*/


// Source: https://www.w3schools.com/howto/howto_js_filter_table.asp
function search_jobs_table() {
	var input, filter, table, tr, td, i, txtValue;
	input = document.getElementById("jobs_search");
	filter = input.value.toUpperCase();
	table = document.getElementById("jobs_table");
	tr = table.getElementsByTagName("tr");
	for (i = 0; i < tr.length; i++) {
	td = tr[i].getElementsByTagName("td")[4];
	if (td) {
		txtValue = td.textContent || td.innerText;
			if (txtValue.toUpperCase().indexOf(filter) > -1) {
				tr[i].style.display = "";
			} else {
				tr[i].style.display = "none";
			}
		}
	}
}


// Source: https://www.w3schools.com/howto/howto_js_sort_table.asp
function sort_jobs_table(n) {
	var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
	table = document.getElementById("jobs_table");
	console.log(table)
	switching = true;
	//Set the sorting direction to ascending:
	dir = "asc"; 
	/*Make a loop that will continue until
	no switching has been done:*/
	while (switching) {
		//start by saying: no switching is done:
		switching = false;
		rows = table.rows;
		/*Loop through all table rows (except the
		first, which contains table headers):*/
		for (i = 1; i < (rows.length - 1); i++) {
			//start by saying there should be no switching:
			shouldSwitch = false;
			/*Get the two elements you want to compare,
			one from current row and one from the next:*/
			x = rows[i].getElementsByTagName("td")[n];
			y = rows[i + 1].getElementsByTagName("td")[n];
			/*check if the two rows should switch place,
			based on the direction, asc or desc:*/
			if (dir == "asc") {
				if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
					//if so, mark as a switch and break the loop:
					shouldSwitch= true;
					break;
				}
			} else if (dir == "desc") {
				if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
					//if so, mark as a switch and break the loop:
					shouldSwitch = true;
					break;
				}
			}
		}
		if (shouldSwitch) {
			/*If a switch has been marked, make the switch
			and mark that a switch has been done:*/
			rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
			switching = true;
			//Each time a switch is done, increase this count by 1:
			switchcount ++;      
		} else {
			/*If no switching has been done AND the direction is "asc",
			set the direction to "desc" and run the while loop again.*/
			if (switchcount == 0 && dir == "asc") {
				dir = "desc";
				switching = true;
			}
		}
	}
}