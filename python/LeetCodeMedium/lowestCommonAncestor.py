class Soluton:
    def lowestCommonAncestor(self, root, p, q):
        if(not root):
            return 
        if(root == p or root == q):
            return root
        
        left_subtree = self.lowestCommonAncestor(root.left, p, q)
        right_subtree = self.lowestCommonAncestor(root.right, p, q)

        # This way we can find the LCA going down the tree until the p and q are found
        # if we find q and p then we return the current root in the recursion stack
        
        if(left_subtree and right_subtree):
            return root 
        
        # if we find q or p but not both we return the subtree in which we find it
        # using q or p as the root
        else:
            return left_subtree if left_subtree else right_subtree