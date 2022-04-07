# Tree

![My image file](https://github.com/EmmaBurkett/CSE212-final-project/blob/main/hidden_files/Capture.PNG)

## What is it?
A binary tree is a data structure made up of instances of a class which are connected like a linked list. Unlike a linked list a tree's node points to two child nodes and does not point to its parent node. 

## Binary Search Tree
Another integral part of a binary search tree (BST) is that a number greater than the current node cannot be placed left of the tree and a number less than the current node cannot be place on the right of the tree. 

Observe the image above and note how it follows this principle. Nodes with values 3 and 5 point to two new nodes. In both cases the node with the larger value is placed on the right of the current node (6 is to the right of 5), and the node with the smaller value is placed on the left of the current node (4 is to the left of 5).

Notice how any number greater than 3 cannot be found on the left of the node and a node less than 3 cannot be found on the right of the node.

The benefit to a BST is that we can search through the data structure in 
O(tree.height). 

Note:
Unlike a linked list, a tree does not store its tail(s) in another class. That means that to access each tail you need to iterate through the nodes above it which can give O(1) time to O(n) time. 

## Balanced Binary Search Trees
Because a Binary Search tree can have a height equal to its number of nodes it can take O(n) time to get to the node on the end. If the tree is 'balanced' or the height of any two subtrees is reasonably similar then it only takes O(log n) time to access the nodes on the end or to find a specific node. 

![My image file](https://github.com/EmmaBurkett/CSE212-final-project/blob/main/hidden_files/image.PNG)

## Searching by O(log n)
In the image above, its subtrees are of equal height, therefore it is a balanced binary search tree. To find the node containing the value 6, start at the root of the tree, 5, and compare 5 to 6. 6 is greater than 5 so look to the right next; this eliminates all the values on the left of 5. Next compare 6 to 8. 6 is less than 8 so look to the left node; this eliminates all the values on the right of 8. The final comparison, 6 vs. 7, shows that 6 is not in the tree at all. 

Note that every time we compared two nodes we halved the remaining nodes that we need to search through to find 6. This is the defenition of O(log n). 

## Recursion
Because each node only points to child nodes and not its parent node, it is necessary to use recursion to move backwards on the tree. To print out a BST from largest to smallest, to the right-most node and print out that node then the one above it. Recursion points to the root node and then recurs the method for the node to the right of the root. Once it has printed out the right node, then that instance of the method ends and the original recur is returned to and the root node is printed out. 

It is impossible to do this with a FOR loop because when we move to the right node we don't have any connections to the root node.


## Operation Performance for a Balanced Binary Search Tree

Operation     | Description       | Performance 
--------------|-------------------|-------------
insert(value) | Insert a value into the tree. | O(log n) - Recursively search the subtrees to find the next available spot. 
remove(value) | Remove a value from the tree. | O(log n) - Recursively search the subtrees to find the value and then remove it. This will require some cleanup of the adjecent nodes. 
contains(value) | Determines if value is in the tree | O(log n) - Recursively search the subtrees to find the value.
traverse_forward | Visit all objects from smallest to largest | O(n) - Recursively traverse the left subtree and then the right subtree. 
traverse_reverse | Visit all objects from larges to smallest | O(n) - Recursively traverse the right subtree and then the left subtree.
height(node) | Determine the height of a node. If the height of the tree is needed, the root node is provided. | O(n) - Recursively traverse the right subtree and then the left subtree.
size() | Return the size of the BST | O(1) - The size is maintained within the BST class. 
empty() | Returns true if the root node is empty. This can also be done by checking the size for 0. | O(1) - The comparison of the root node or the size.

## To-Do List:
This algorithm will take my to-do list, and create a Binary Search Tree based on how long each task will take me. Then it will print out my to_do list. 

``` python
class ToDoList:

    class Task:
        def __init__(self, task, duration):
            self.left = None
            self.right = None
            self.task = task
            self.duration = duration
    
    def __init__(self):
        self.root = None

    def create_task(self, task, duration, node):
        """ This method searches the current tree to find an empty 
            location for the specific node. If the specific
            node's duration is smaller place the task to the left of 
            the current node. This method does not allow for nodes with
            identical durations. 
        """
        # If duration < node.duration then the task belongs on the left side.
        if duration < node.duration:

            # If there is an empty spot fill that spot with a task.
            if node.left is None:

                # The only connection you need to make betweeen a node 
                # on the tree to a new_node is a pointer to the new node
                # from the node. The new node does not point back to 
                # the previous node.
                node.left = self.Task(task, duration)
            else:

                # Recur to the left and check for open spots. 
                self.create_task(task, duration, node.left)
        elif duration != node.duration:

            # The data belongs on the right side.
            if node.right is None:

                # Fill the empty spot!
                node.right = self.Task(task, duration)
            else:

                # Recur to the right and check for open spots.
                self.create_task(task, duration, node.right)
    
    def display_tree(self, node):
        """The method recurs until it reaches the right-most node. 
           After it has reached the right-most node it will print the 
           task then check if there is a node to the left of the 
           right-most node. If there is a node to the left, then the 
           function recurs, does the same check for the right of this 
           new node, and then prints the node. 
        """
        # Iterate through every node!
        if node is not None:

            # Recure this function all the way to the right-most node
            # before printing.
            # Check the right of the current node.
            self.display_tree(node.right)

            # Print current node's task.
            print(node.task)

            # Check to the left of the current node.
            self.display_tree(node.left)

to_do = ToDoList()
to_do.root = to_do.Task("Clean room", 5)
to_do.create_task("Mini-assignment", 20, to_do.root)
to_do.create_task("Make food", 60, to_do.root)
to_do.create_task("Laundry", 75, to_do.root)
to_do.create_task("Help roommate", 30, to_do.root)
to_do.create_task("Assignment", 120, to_do.root)
to_do.create_task("Final", 180, to_do.root)
to_do.create_task("Sharpen Pencil", 2, to_do.root)
to_do.create_task("Update Computer", 100, to_do.root)
to_do.create_task("Dust", 10, to_do.root)
to_do.create_task("Large Assignment", 150, to_do.root)

to_do.display_tree(to_do.root)
```

## [Coding Challenge](https://github.com/EmmaBurkett/CSE212-final-project/blob/main/coding_challenges/to_do_tree.py): 
As a student I often find myself asking the question 'what can I get done in the time that I have?' Sometimes I have five minutes and I pick up my room, sometimes I have 6 hours and I work through a few of my larger assignments. 

Your challenge is to add an additional method that returns the largest task which can be completed in the time given. 

#### [Solution](https://github.com/EmmaBurkett/CSE212-final-project/blob/main/coding_challenges/Answers/to_do_tree_answer.py)


###### Vocabulary
Term | Definition
-----|----------------------------------------------------------------
Node | An entry in a tree that contains both the value and pointers to any children nodes.
Child | A child is a node connected from a parent node.
Leaf | A leaf is a node that has no children.
Parent | A parent is a node that connects to children nodes.
Root | The first parent in a tree.
Subtree | Subset of a tree made by selecting a node to be the root and including all the children from that node. 