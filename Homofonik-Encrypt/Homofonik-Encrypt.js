const chalk = require('chalk');

class Homofonik {
    constructor() {
        this.table_homofonik = {
            A: ["BU", "CP", "AV", "AH", "BT", "BS", "CQ"],
            B: ["AT"],
            C: ["DL", "BK", "AU"],
            D: ["BV", "DY", "DM", "AI"],
            E: ["DK", "CO", "AW", "BL", "AA", "CR", "BM", "CS", "AF", "AG", "BO", "BN", "BE"],
            F: ["BW", "CM", "CN"],
            G: ["DN", "BJ"],
            H: ["AS", "CL", "CK"],
            I: ["DJ", "BI", "AX", "CJ", "AB", "BP", "CU", "CT"],
            J: ["BX"],
            K: ["DI"],
            L: ["AR", "BH", "CI", "AJ"],
            M: ["DH", "BG", "AY"],
            N: ["BY", "DG", "DF", "CH", "AC", "BR", "DU", "DT"],
            O: ["DZ", "BF", "DX", "AK", "CG", "BQ", "DR"],
            P: ["BZ", "DE", "AZ"],
            Q: ["DD"],
            R: ["AQ", "DC", "DQ", "AL", "CE", "CF", "CV", "DS"],
            S: ["AP", "AN", "AO", "CD", "DW", "DV"],
            T: ["CB", "DB", "DP", "CC", "AD", "CY", "CW", "CX", "AE"],
            U: ["CA", "AM", "BA"],
            V: ["BB"],
            W: ["CZ"],
            X: ["BD"],
            Y: ["DO", "DA"],
            Z: ["BC"]
        }

        this.divide_by_two = (str) => {
            let Arr = [];
            let getStr = str.split(' '); // menghilangkan spasi pada string
            getStr = getStr.join(''); // menggabungkan beberapa elemen pada array
            for (let i = 0; i < getStr.length; i += 2) {
                Arr.push(getStr.slice(i, i + 2));
            }
            return Arr;
        }
    }


    encrypt(plain) {
        let chipArr = [];
        for (let i = 0; i < plain.length; i++) {
            if (plain[i] != " "){
                let subChip = this.table_homofonik[plain[i]].length;
                let getRandom = Math.floor(Math.random() * subChip);
                chipArr.push(this.table_homofonik[plain[i]][getRandom]);
            } else {
                chipArr.push(plain[i]);
            }
        }
        console.log(chalk.greenBright("\n== RESULT =="));
        console.log(`Chipertext: ${chipArr.join(' ')}`);
    }

    decrypt(chiper) {
        let plainArr = [];

        // membagi 2 2 chipertext
        let chipArr = this.divide_by_two(chiper);

        for(let j = 0; j < chipArr.length; j++){
            Object.entries(this.table_homofonik).forEach(([key, value]) => {
                for (let i = 0; i < value.length; i++) {
                    if (value[i] == chipArr[j]) {
                        plainArr.push(key);
                    }
                }
            });
        }

        console.log(chalk.greenBright("\n== RESULT =="));
        console.log(`Plaintext: ${plainArr.join('')}`);
    }
}

module.exports = Homofonik;