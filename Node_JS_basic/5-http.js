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
      res.end('Cannot load the database');
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
