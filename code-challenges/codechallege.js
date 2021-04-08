// CHALLENGE - counting bits
// Write a function called countTheBits that accepts a single numeric argument that will be an integer.
// The function should return the number of bits set to 1 in the number's binary representation.

const countTheBits = (num) => {
  if (num == 0){
    return 0
  }
  return (num & 1) + countTheBits(num >> 1)
}

// CHALLENGE - Find shortest word 
const findShort = (string) => {
    const splitString = string.split(' ')

    let shortest = splitString[0].length
    
    splitString.forEach((word) => {
        if (word.length < shortest){
            shortest =word.length;
        }
    })

    console.log(shortest)
}

findShort("bitcoin take over the world maybe who knows perhaps")
// returns 3
findShort("turns out of random test cases are easier than writing out basic ones") 
// returns 2

