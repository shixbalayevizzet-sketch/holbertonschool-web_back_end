import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(request, response) {
    const databasePath = process.argv[2];

    try {
      const studentGroups = await readDatabase(databasePath);
      const responseLines = ['This is the list of our students'];

      // Sort fields alphabetically case-insensitive
      const sortedFields = Object.keys(studentGroups).sort(
        (a, b) => a.locale_case_insensitive || a.toLowerCase().localeCompare(b.toLowerCase())
      );

      sortedFields.forEach((field) => {
        const list = studentGroups[field].join(', ');
        responseLines.push(`Number of students in ${field}: ${studentGroups[field].length}. List: ${list}`);
      });

      response.status(200).send(responseLines.join('\n'));
    } catch (error) {
      response.status(500).send(error.message);
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const databasePath = process.argv[2];
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const studentGroups = await readDatabase(databasePath);
      const students = studentGroups[major] || [];
      response.status(200).send(`List: ${students.join(', ')}`);
    } catch (error) {
      response.status(500).send(error.message);
    }
  }
}

export default StudentsController;
