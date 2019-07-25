

const wellFormedString = (s) =>{
    const pairs = {
        '(':')',
        '[':']',
        '{':'}',
    }

    const stack = []
    for(const letter of s){
        if(letter in pairs)
            stack.push(letter)
        else{
            if(pairs[stack.pop()] != letter)
                return false
        }
    }
    return true
}

console.log(wellFormedString('(({}))'))