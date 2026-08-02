const fs = require('fs');

const countStudents = (dataPath) => {
  try {
    // Read the file synchronously with utf8 encoding
    const fileContent = fs.readFileSync(dataPath, 'utf-8');
    
    // Split content by lines and filter out empty lines
    const lines = fileContent
      .split('\n')
      .map((line) => line.trim())
      .filter((line) => line.length > 0);

    // If there's only a header or the file is completely empty
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    // The first line is the header
    const studentLines = lines.slice(1);
    console.log(`Number of students: ${studentLines.length}`);

    // Object to store fields and their corresponding first names
    const fields = {};

    studentLines.forEach((line) => {
      const studentData = line.split(',');
      const firstname = studentData[0];
      const field = studentData[3];

      if (firstname && field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    });

    // Log the statistics for each field
    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
