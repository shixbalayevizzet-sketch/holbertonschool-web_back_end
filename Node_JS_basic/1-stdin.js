#!/usr/bin/node

process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (data) => {
  process.stdout.write(`Your name is: ${data}`);
});

process.on('end', () => {
  console.log('This important software is now closing');
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
