#!/usr/bin/node
const fs = require('fs');

const fArg = fs.readFilesync(process.argv[2]).toString();
const sArg = fs.readFilesync(process.argv[3]).toString();
fs.writeFilesync(process.argv[4], fArg + sArg);
