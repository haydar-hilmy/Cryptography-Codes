class Rail_Fence {
    encrypt(alg, plain) {

        // membuat subarray
        let chipArr = new Array(alg);
        for (let i = 0; i < alg; i++) {
            chipArr[i] = [];
        }

        let i = 0;
        while (i < plain.length) {
            let j = 0;
            while (j < alg - 1 && i < plain.length) {
                console.log(`${plain[i]} : baris-${j} : iterasi-${i}`);
                chipArr[j].push(plain[i])
                j += 1;
                i += 1;
            }
            while (j > 0 && i < plain.length) {
                console.log(`${plain[i]} : baris-${j} : iterasi-${i}`)
                chipArr[j].push(plain[i])
                j -= 1;
                i += 1;
            }
        }
    }

    decrypt(alg, chiper) {

        // membuat subarray
        let plainArr = new Array(alg);
        for (let i = 0; i < alg; i++) {
            plainArr[i] = [];
        }

        let i = 0;
        while (i < chiper.length) {
            let j = 0;
            while (j < alg - 1 && i < chiper.length) {
                if(k == j){
                    console.log(`* : baris-${j} : iterasi-${i}`);
                    plainArr[j].push("*");
                }
                j += 1;
                i += 1;
            }
            while (j > 0 && i < chiper.length) {
                if(k == j){
                    console.log(`* : baris-${j} : iterasi-${i}`);
                    plainArr[j].push("*");
                }
                j -= 1;
                i += 1;
            }
        }

    }
}

module.exports = Rail_Fence;