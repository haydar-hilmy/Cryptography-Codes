const readline = require("readline");
const Rail_Fence = require('./Rail-Fence-Encrypt')
const chalk = require('chalk');
const { exit } = require("process");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// interface will be show
console.log(chalk.yellowBright("=-=-= TRANSPOTITION RAIL FENCE =-=-="));
console.log("[1] Encrypt");
console.log("[2] Decrypt");
console.log("[3] Exit");

const RF = new Rail_Fence;

rl.question("choose: ", (choose) => {
    if (choose == "3") {
        console.log(chalk.blueBright("\nProgrammed by Haydar"));
        rl.close();
        exit(1);
    }
    rl.question("plain/chiper: ", (plain_chiper) => {
        rl.question("algoritma: ", (alg) => {
            try {
                if (choose == "1") {
                    RF.encrypt(alg, plain_chiper);
                } else if (choose == "2") {
                    RF.decrypt(alg, plain_chiper);
                }
            } catch (error) {
                throw error;
            } finally {
                console.log(chalk.blueBright("\nProgrammed by Haydar"));
                rl.close();
            }
        });
    });
});