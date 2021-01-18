def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return findFirst(s, t)
    def findFirst(s, t):
        return s != None and (equals(s, t) or findFirst(s.left, t) or findFirst(s.right, t))
    def equals(s, t):
        if s == t == None:
            return True
        if s == None or t == None:
            return False
        return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)
    