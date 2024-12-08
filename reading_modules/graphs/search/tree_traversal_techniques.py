#  https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

# [****Inorder Traversal****](https://www.geeksforgeeks.org/inorder-traversal-of-binary-tree/) ****:****

'''
```md
Inorder traversal visits the node in the order: ****Left -> Root -> Right****

![Preorder-Traversal-of-Binary-Tree](https://media.geeksforgeeks.org/wp-content/uploads/20240429124538/Preorder-Traversal-of-Binary-Tree.webp)
```
'''
# A function to do inorder tree traversal


def printInorder(root):

    if root:

        # First recur on left child
        printInorder(root.left)

        # Then print the data of node
        print(root.val, end=" "),

        # Now recur on right child
        printInorder(root.right)
