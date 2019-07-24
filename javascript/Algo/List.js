const ListNode = require("./ListNode");


class List{
    constructor(value){
        this.head = new ListNode(value);
    }

    arrayToList(arr){
        // This function overrides the values that are in the List.
        let currentNode = this.head;
        for(const i of arr){
            currentNode.nextP = new ListNode(i);
            currentNode = currentNode.nextP;
        }
        this.head = this.head.nextP
        return this.head;
    }

    printList(){
        let currentNode = this.head;
        while(currentNode){
            console.log(currentNode.data);
            currentNode = currentNode.nextP
        }
    }
}


let newList = new List();
newList.arrayToList([1,2,3,4]);
newList.printList();
newList.arrayToList([1,2,3,4,6,6]);
newList.printList();
