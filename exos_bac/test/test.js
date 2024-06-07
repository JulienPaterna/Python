str = "qkhsfb2aoigd1ugks8d5qksjbfq9"
tab = []
for (const elem of str) {
    if (parseInt(elem)) {
        tab.push(elem)
    } 
}
num_1 = tab[0]
num_2 = tab[tab.length - 1]
console.log(parseInt(num_1+num_2))
num = parseInt(tab[0]+tab[1])
// num = parseInt(tab.join(''))
// console.log(num)
