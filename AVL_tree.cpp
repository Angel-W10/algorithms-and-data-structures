#include <iostream>
#include <string>

class Node {

public:

	//parameters
	Node* left;
	Node* right;
	int value;

	//functions

	Node() {
		value = 0;
		left = NULL;
		right = NULL;
	}

	Node(int v) {
		value = v;
		left = NULL;
		right = NULL;
	}
};


class Tree {

public:
	Node* root;

	Tree() {
		root = NULL;
	}

	//functions

	bool isEmpty() {
		if (root == NULL) {
			return true;
		}
		else {
			return false;
		}
	}

	int get_height(Node* n) {

		if (n == NULL) { //((n->left == NULL)&&(n->right==NULL)) {
			return -1;
		}

		else {

			int l_height = get_height(n->left);
			int r_height = get_height(n->right);
			//std::cout << n->value << " " << l_height << " " << r_height << std::endl;

			if (l_height > r_height) {
				return (l_height + 1);
			}
			else {
				return (r_height + 1);
			}

		}
	}


	int get_bal(Node* n) {

		if ((n->left == NULL) && (n->right == NULL)) {
			return -1;
		}

		else {
			int bal = get_height(n->left) - get_height(n->right);
			return bal;
		}

	}


	//Node* insert_node(Node* new_node) {

	//	if (root == NULL) {
	//		root = new_node;
	//	}
	//	else {
	//		Node* temp = root;

	//		while (temp != NULL) {

	//			/*if ((new_node->value < temp->value) && (temp->left == NULL)) {
	//				temp->left = new_node;
	//				std::cout << "saved to left" << std::endl;
	//				break;
	//			}*/
	//			if (new_node->value < temp->value) {
	//				temp = temp->left;
	//				temp = insert_node(new_node);
	//			}
	//			/*else if ((new_node->value > temp->value) && (temp->right == NULL)) {
	//				temp->right = new_node;
	//				std::cout << "saved to right" << std::endl;
	//				break;
	//			}*/
	//			else {
	//				temp = temp->right;
	//				temp = insert_node(new_node);
	//			}
	//		}
	//	}
	//	/*if (new_node->value > root->value) {
	//		root->right = insert_node(new_node);
	//	}
	//	else if (new_node->value < root->value) {
	//		root->left = insert_node(new_node);
	//	}
	//	else {
	//		return root;
	//	}*/

	//}

	Node* r_left(Node* n) {
		Node* A = n->right;
		Node* B = A->left;

		A->left = n;
		n->right = B;
		return A;
	}

	Node* r_right(Node* n) {
		Node* A = n->left;
		Node* B = A->right;

		A->right = n;
		n->left = B;
		return A;
	}


	Node* insert_node(Node* new_node, Node* r) {
		//for the first entry
		if (r == NULL) {
			//std::cout << "here" << std::endl;
			r = new_node;
			return r;
		}
		//Node* temp = root;

		//move on to the left node
		if (new_node->value < r->value) {
			r->left = insert_node(new_node, r->left);
		}

		else if (new_node->value > r->value) { //to the right node
			r->right = insert_node(new_node, r->right);
		}

		else {
			return r;
		}

		//call the function to get the balance factor
		int bal = get_bal(r);

		if ((bal < -1) && (new_node->value > r->right->value)) {
			//left rotation
			return r_left(r);
		}

		if ((bal < -1) && (new_node->value < r->right->value)) {
			//right left rotation
			r->right = r_right(r->right);
			return r_left(r);
		}

		if ((bal > 1) && (new_node->value < r->left->value)) {
			//right rotation
			return r_right(r);
		}

		if ((bal > 1) && (new_node->value > r->left->value)) {
			//left right rotation
			r->left = r_left(r->left);
			return r_right(r);
		}

		return r;
	}



	// printing functions

	void pre_print(Node* n) {
		if (n == NULL) { // last element
			//std::cout << "EMPTY";
			return;
		}
		std::cout << n->value << " ";

		pre_print(n->left);

		pre_print(n->right);
	}

	void post_print(Node* n) {
		if (n == NULL) { // last subtree/node
			//std::cout << "EMPTY";
			return;
		}

		post_print(n->left); // left subtree/node

		post_print(n->right); //right subtree/node

		std::cout << n->value << " ";
	}

	void in_print(Node* n) {

		if (n == NULL) { // last subtree/node
			//std::cout<<"EMPTY" ;
			return;
		}

		in_print(n->left); //left subtree/node

		std::cout << n->value << " ";

		in_print(n->right); //right subtree/node
	}

	Node* leftmax(Node* n) {
		Node* temp = n;

		while (temp->right != NULL) {
			temp = temp->right;
		}
		return temp;
	}


	//delete a node & check if its balanced
	Node* delete_node(Node* n, Node* root) {
		//base case
		if (root == NULL) {
			return root;
		}

		else if (n->value < root->value) {
			root->left = delete_node(n, root->left);
		}

		else if (n->value > root->value) {
			root->right = delete_node(n, root->right);
		}

		else { //n->value is same as root->value

			if (root->left == NULL) {
				Node* temp = root->right;
				delete root;
				return temp;
			}

			else if (root->right == NULL) {
				Node* temp = root->left;
				delete root;
				return temp;
			}

			else { //node with nodes on both left and right

				Node* temp = leftmax(root->left);
				root->value = temp->value;
				root->left = delete_node(temp, root->left);

			}

		}

		int bal = get_bal(root);

		if (bal == 2 && get_bal(root->left) >= 0) {
			return r_right(root);
		}
		else if (bal == 2 && get_bal(root->left) == -1) {
			root->left = r_left(root->left);
			return r_right(root);
		}
		else if (bal == -2 && get_bal(root->right) <= -0) {
			return r_left(root);
		}
		else if (bal == -2 && get_bal(root->right) == 1) {
			root->right = r_right(root->right);
			return r_left(root);
		}

		return root;

	}

};





int main() {

	using namespace std;

	Tree my_tree;
	//cout << my_tree.root->value << endl;
	//cout << "here" << endl;
	string input;
	cin >> input;
	while (input != "PRE" || input != "POST" || input != "IN") {

		if (input[0] == 'A') {
			//insert Node
			int val = stoi(input.substr(1, input.length()));
			Node* new_node = new Node(val);
			my_tree.root = my_tree.insert_node(new_node, my_tree.root);
			//cout << "created a new node with value: " << val << endl;
			//cout << "the root is: " << my_tree.root->value << endl;
		}
		else if (input[0] == 'D') {
			//delete Node
			int val = stoi(input.substr(1, input.length()));
			Node* new_node = new Node(val);
			my_tree.root = my_tree.delete_node(new_node, my_tree.root);
			//cout << "deleted a new node with value: " << val << endl;
			//cout << "the root is: " << my_tree.root->value << endl;

		}
		if (my_tree.isEmpty() == true) {
			cout << "EMPTY";
			break;
		}
		else
		{
			if (input == "PRE") {
				my_tree.pre_print(my_tree.root);
				break;
			}if (input == "POST") {
				my_tree.post_print(my_tree.root);
				break;
			}if (input == "IN") {
				my_tree.in_print(my_tree.root);
				break;
			}
		}


		cin >> input;
	}

	return 0;
}
