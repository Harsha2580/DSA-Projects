function calculateAge() {
    // Input date and time
    var inputDate = new Date(document.getElementById("dobInput").value);
    
    // Current date and time
    var now = new Date();
    
    // Calculate the difference in milliseconds
    var ageInMilliseconds = now - inputDate;

    // Convert milliseconds to years with 9 decimal places
    var ageInYears = ageInMilliseconds / (1000 * 60 * 60 * 24 * 365.25);
    
    // Display the age with 9 decimal places
    document.getElementById("age").innerHTML = ageInYears.toFixed(9);
}

// Update age every 10 milliseconds for a faster change
setInterval(calculateAge, 10);
