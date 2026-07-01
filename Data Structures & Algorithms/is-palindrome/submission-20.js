class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const isAlnum = [...s.toLowerCase()].filter(ch => /[a-z0-9]/i.test(ch))
        let LP = 0
        let RP = isAlnum.length - 1        

        while (LP < RP){
            console.log(isAlnum[LP])
            console.log(isAlnum[RP])
            if (isAlnum[LP] !== isAlnum[RP]) {
                return false
            }
            LP++;
            RP--;
        }
        return true
        // const alnumList = s.split("")
        //                    .filler(ch => /[0-9A-Za-z]/i.test(ch))
        //                    .join("")
        console.log([...s])
        console.log(isAlnum)
        return false
    }
}
