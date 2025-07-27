var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Mentors");

function doGet(e) {
  var userEmail = Session.getActiveUser().getEmail();

  // 🔒 Restrict access to @vcu.edu users only
  if (!userEmail.endsWith("@vcu.edu")) {
    return HtmlService.createHtmlOutputFromFile("login");
  }

  // Show main app UI
  return HtmlService.createHtmlOutputFromFile("index").setTitle(
    "VCU Engineering - Mentor Career Chat"
  );
}
// Get all mentors (including full ones) and signed-up students
function getMentors() {
  var data = sheet.getDataRange().getValues();
  var headers = data[0];

  // Map header indexes
  var nameIdx = headers.indexOf("First & Last Name");
  var areaOfFocusIdx = headers.indexOf(
    "Your area of focus (i.e. process engineering, full stack development, product R&D, etc.)"
  );
  var industryIdx = headers.indexOf("Industry you can share about.");
  var companyIdx = headers.indexOf("Company");
  var emailIdx = headers.indexOf("Email Address");
  var slotIdx = headers.indexOf("Available Slots");
  var signupIdx = headers.indexOf("Signed-Up Students");

  // Collect all signed-up students
  var allSignedUpStudents = [];
  for (var i = 1; i < data.length; i++) {
    var signedUp = data[i][signupIdx] || "";
    if (signedUp) {
      allSignedUpStudents.push(...signedUp.split(",").map((e) => e.trim()));
    }
  }

  PropertiesService.getScriptProperties().setProperty(
    "allSignedUpStudents",
    JSON.stringify(allSignedUpStudents)
  );

  // Return all mentors with their data
  return data.slice(1).map(function (row) {
    var signedUp = row[signupIdx]
      ? row[signupIdx].split(",").map((e) => e.trim())
      : [];

    return {
      name: row[nameIdx],
      areaOfFocus: row[areaOfFocusIdx],
      industry: row[industryIdx],
      company: row[companyIdx],
      email: row[emailIdx],
      availableSlots: parseInt(row[slotIdx]) || 0,
      signedUpStudents: signedUp,
    };
  });
}

// Book a slot with a mentor
function bookSlot(mentorName, studentEmail) {
  studentEmail = studentEmail.trim().toLowerCase();

  // Validate email domain
  if (!studentEmail.endsWith("@vcu.edu")) {
    return {
      success: false,
      message: "Only VCU student emails (ending with @vcu.edu) are allowed.",
    };
  }

  // Check if student has already booked any mentor
  var data = sheet.getDataRange().getValues();
  var headers = data[0];
  var signupIdx = headers.indexOf("Signed-Up Students");

  for (var i = 1; i < data.length; i++) {
    var signedUp = data[i][signupIdx] || "";
    if (
      signedUp
        .split(",")
        .map((e) => e.trim())
        .includes(studentEmail)
    ) {
      return { success: false, message: "You've already booked a session." };
    }
  }

  // Find the selected mentor
  var nameIdx = headers.indexOf("First & Last Name");
  var slotIdx = headers.indexOf("Available Slots");
  var emailIdx = headers.indexOf("Email Address");
  var areaOfFocusIdx = headers.indexOf("Your area of focus...");
  var industryIdx = headers.indexOf("Industry you can share about.");
  var companyIdx = headers.indexOf("Company you can share about...");

  for (var i = 1; i < data.length; i++) {
    if (data[i][nameIdx] === mentorName && data[i][slotIdx] > 0) {
      // Decrease available slots
      sheet.getRange(i + 1, slotIdx + 1).setValue(data[i][slotIdx] - 1);

      // Add student to list
      var currentStudents = data[i][signupIdx] || "";
      sheet
        .getRange(i + 1, signupIdx + 1)
        .setValue(
          currentStudents + (currentStudents ? ", " : "") + studentEmail
        );

      // Get mentor info for email
      var mentorEmail = data[i][emailIdx];
      var areaOfFocus = data[i][areaOfFocusIdx];
      var industry = data[i][industryIdx];
      var company = data[i][companyIdx];

      // Send confirmation email
      MailApp.sendEmail({
        to: studentEmail,
        subject: "Career Chat Confirmation with " + mentorName,
        body:
          "Great news! Your career chat with " +
          mentorName +
          " has been confirmed.\n\n" +
          "Here are their details:\n" +
          "Email: " +
          mentorEmail +
          "\n" +
          "Area of Focus: " +
          areaOfFocus +
          "\n" +
          "Industry: " +
          industry +
          "\n" +
          "Company: " +
          company +
          "\n\n" +
          "Please reach out to them directly to schedule your call.",
      });

      return {
        success: true,
        message: "Successfully booked with " + mentorName + "!",
      };
    }
  }

  return { success: false, message: "This mentor has no available slots." };
}
