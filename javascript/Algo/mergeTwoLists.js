const ListNode = require("./ListNode");

// Creating a simple lists
const L1 = new ListNode(2);
L1.nextP = new ListNode(5);
L1.nextP.nextP = new ListNode(7);

const L2 = new ListNode(3);
L2.nextP = new ListNode(11);

const mergeLists = (L1, L2)=>{
    let merging = new ListNode()
    const dummyhead = merging; // We have to keepTrack of the beggining of the resulting list

    while(L1 && L2){
        if(L1.data < L2.data){
            merging.nextP = L1;
            L1 = L1.nextP;
        }
        else{
            merging.nextP = L2;
            L2 = L2.nextP;
        }
        merging = merging.nextP;
    }

    merging.nextP = L1 || L2;
    return dummyhead.nextP;

}

const printList = (L) =>{
    while(L){
        console.log(L.data);
        L = L.nextP
    }
}
let merge = mergeLists(L1, L2);
printList(merge)