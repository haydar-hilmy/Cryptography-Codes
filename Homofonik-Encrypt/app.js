const readline = require("readline");
const Homofonik = require('./Homofonik-Encrypt')
const chalk = require('chalk');
const { exit } = require("process");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// interface will be show
console.log(chalk.yellowBright("=-=-= HOMOFONIK SUBSTITUTIONS =-=-="));
console.log("[1] Encrypt");
console.log("[2] Decrypt");
console.log("[3] Exit");

const hom = new Homofonik;

rl.question("choose: ", (choose) => {
    if (choose == "3") {
        console.log(chalk.blueBright("\nProgrammed by Haydar"));
        rl.close();
        exit(1);
    }
    rl.question("plain/chiper: ", (plain_chiper) => {
        try {
            if (choose == "1") {
                hom.encrypt(plain_chiper);
            } else if (choose == "2") {
                hom.decrypt(plain_chiper);
            }
        } catch (error) {
            throw error;
        } finally {
            console.log(chalk.blueBright("\nProgrammed by Haydar"));
            rl.close();
        }
    });
});