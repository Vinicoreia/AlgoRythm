/* 
In a Particular board game a player has to try to advance through a sequence of positions.
Each position has a nonnegative integer associated with it, representing the maximum you can advance
from that position in one move. You begin in the first position and win if you can reach the end.

Example
input: [3,3,1,0,2,0,1]
output: True
explanation: At index 0 you can advance a maximum of 3 steps, you choose to advance 1
             now you are at index 1, again you can advance a maximum of 3 steps.
             You choose to advance 3 steps and now you are at index 4.
             You can advance a maximum of 2 steps now, you advance 2 and then you win since you are in the last position

input: [3,2,0,0,2,0,1]
output: false
explanation: you are at index 0, you can choose to advance a maximum of 3 positions, that would leave you at
             a position that you can not reach the end, no matter how many steps you take from the begginning
            
*/


// This may seem as a difficult problem at first but we only have to compute how far can we reach from every position
// from the beggining of the array until the end.



const canReachEnd = (A) =>{
    let reach = 0; // how far can I reach from this position
    let i =0;

    while ( i <= reach && reach < A.length - 1 ){
        reach = Math.max(reach, A[i] + i);
        i++;
    }
    return reach >= A.length -1;
}
console.log(canReachEnd([3,2,0,0,2,0,1]));
console.log(canReachEnd([3,3,1,0,2,0,1]));