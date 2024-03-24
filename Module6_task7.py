def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    with open(path_to_log_file, 'r') as file:
        file_list = file.readlines()
        root_num = int(file_list[0][30:36])
        root = BinaryTreeNode(val=root_num, left=None, right=None)
        tree = {}
        for line in file_list:
            if line.startswith('INFO'):
                node_num = int(line[30:36])
                tree[node_num] = BinaryTreeNode(node_num)
            elif line.startswith('DEBUG') and 'left' in line:
                node_left = int(line[73:79])
                tree[node_num] = BinaryTreeNode(
                    val=node_num, left=BinaryTreeNode(node_left), right=None)
            elif line.startswith('DEBUG') and 'right' in line:
                node_right = int(line[74:80])
                tree[node_num] = BinaryTreeNode(
                    val=node_num, left=BinaryTreeNode(node_left), right=BinaryTreeNode(node_right))
        return root