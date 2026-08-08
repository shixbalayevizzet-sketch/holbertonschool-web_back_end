const express = require('express');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];
const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const responseText = ['This is the list of our students'];

  try {
    let output = '';
    const originalLog = console.log;
    console.log = (d) => {
      output += `${d}\n`;
      originalLog(d);
    };

    await countStudents(database);

    console.log = originalLog;
    responseText.push(output.trim());
    res.send(responseText.join('\n'));
  } catch (error) {
    res.send('This is the list of our students\nCannot load the database');
  }
});

app.listen(1245);

module.exports = app;
