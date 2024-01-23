// Retrieve data from localStorage
var jsonData = localStorage.getItem("medicineData");

// Parse JSON data
var data = JSON.parse(jsonData);

// Display the data on the page
document.getElementById("dataDisplay").innerText = JSON.stringify(data, null, 2);





