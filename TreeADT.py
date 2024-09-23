class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        # Adding a child node to the current node
        self.children.append(child_node)

    def remove_child(self, child_node):
        # Removing a child node from the current node
        self.children = [child for child in self.children if child != child_node]

    def get_data(self):
        return self.data
    def get_children(self):
        return self.children
    
class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def get_root(self):
        return self.root
    def traverse(self, node, level=0):
        # Pre-order traversal of the tree
        print(" " * level * 2, node.get_data())
        for child in node.get_children():
            self.traverse(child, level + 1)

##USAGE
# Create the root of the tree
tree = Tree("Root")

# Create child nodes
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
child3 = TreeNode("Child 3")

# Add children to root
tree.get_root().add_child(child1)
tree.get_root().add_child(child2)

# Add children to child1
child1.add_child(TreeNode("Child 1.1"))
child1.add_child(TreeNode("Child 1.2"))

# Add a child to child2
child2.add_child(child3)

# Add children to child3
child3.add_child(TreeNode("Child 3.1"))

# Traverse the tree
tree.traverse(tree.get_root())
