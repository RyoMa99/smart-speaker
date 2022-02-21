const { exec } = require("child_process");

exec(`paplay ${__dirname}/test.wav`, (err, stdout, stderr) => {
  if(err){
    console.log(`stderr: ${stderr}`);
    return;
  }
});