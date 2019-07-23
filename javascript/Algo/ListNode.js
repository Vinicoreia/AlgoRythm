class ListNode{
    constructor(data=null, nextP = null){
        this.data = data;
        this.nextP = nextP;
    }
}

module.exports = ListNode;


// let b = new ListNode(valor, ponteiro);
// if you want to require you can create a new instance by
// const Node = require("./ListNode")
// let head = Node(value, nextPointer);
