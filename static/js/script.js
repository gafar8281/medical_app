function addItem() {
    // Get form values
    var medicineName = document.getElementById("medicinename").value;
    var batchNo = document.getElementById("batchno").value;
    var medicineCategory = document.getElementsByName("med-cat")[0].value;
    var expiryDate = document.getElementById("expdate").value;
    var replacementDate = document.getElementById("repdate").value;

    // Create a data object with the entered values
    var data = {
        "Medicine Name": medicineName,
        "Batch No.": batchNo,
        "Medicine Category": medicineCategory,
        "Expiry Date": expiryDate,
        "Replacement Date": replacementDate
    };

    // Convert the data object to a JSON string
    var jsonData = JSON.stringify(data);

    // Use sessionStorage to store the data temporarily
    sessionStorage.setItem("medicineData", jsonData);

    // Redirect to text.html
    window.location.href = "/templates/text.html";
}

