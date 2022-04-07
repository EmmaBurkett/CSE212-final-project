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
        if duration < node.duration:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = self.Task(task, duration)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self.create_task(task, duration, node.left)
        elif duration != node.duration:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = self.Task(task, duration)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self.create_task(task, duration, node.right)
    
    def display_tree(self, node):
        """The function recurs until it reaches the right most node. 
           After it has reached the right-most node it will print the 
           task then check if there is a node to the left of the 
           right-most node. If there is a node to the left, then the 
           function recurs, does the same check for the right of this 
           new node, and then prints the node. 
        """
        # Iterate through every node!
        if node is not None:

            # Recure this function all the way to the right most node
            # before printing.
            # Check the right of the current node.
            self.display_tree(node.right)

            # Print current node's task.
            print(node.task)

            # Check to the left of the current node.
            self.display_tree(node.left)

    
    def find_task(self, node, duration):
        """ This method will check for the largest possible task to do
            inside a flexible duration. 
        """

        # If the node doesn't have a match in the tree search for the 
        # next possible duration.
        if node is None: 
            self.find_task(self.root, duration - 1)
        
        # If the duration is greater than the node's duration move to
        # the right node.
        elif duration > node.duration:
            self.find_task(node.right, duration)

        # If the duration is less than the node's duration move to the 
        # left node.
        elif duration < node.duration:
            self.find_task(node.left, duration)
        
        # If the node has been found print that node and recur no more!
        elif duration == node.duration:
            print(node.task)
            return
            


   

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

to_do.find_task(to_do.root, 179)
