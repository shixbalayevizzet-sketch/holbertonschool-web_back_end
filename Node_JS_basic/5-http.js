const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    
    try {
      // Capture console.log output or let countStudents write to stdout,
      // but standard Holberton tests expect countStudents to print to console
      // and the HTTP response to contain the same text or be streamed.
      // Let's capture/collect or rely on standard execution depending on requirements.
      // Usually, countStudents logs to stdout. To pipe it to the response or collect it:
      
      // We can temporarily override console.log to capture the output:
      let output = '';
      const originalLog = console.log;
      console.log = (d) => {
        output += `${d}\n`;
        originalLog(d);
      };

      await countStudents(database);

      console.log = originalLog;
      res.end(output.trim());
    } catch (error) {
      res.end('This is the list of our students\nCannot load the database');
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
