


const RPN = (s) =>{
    const arr = s.split(' ');
    const operations = {
        '+': (x,y)=> x + y,
        '*': (x,y)=> x * y,
        '/': (x,y)=> y - x,
        '-': (x,y)=> y - x,
    }
    const result = [];
    for(const token of arr){
        !isNaN(parseInt(token))
        ? result.push(parseInt(token))
        : result.push(operations[token](result.pop(), result.pop()))
    }
    return result;
}

console.log(RPN('3 4 + 2 * 1 +'))