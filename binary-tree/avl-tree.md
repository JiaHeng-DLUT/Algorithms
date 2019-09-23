# AVL Tree

* AVL 树仍然是一棵二叉查找树，只是在其基础上增加了“平衡”的要求。
* 所谓平衡是指，对 AVL 树的任意结点来说，其左子树与右子树的高度之差的绝对值不超过 1，其中左子树与右子树的高度之差称为该结点的平衡因子。
* 只要能随时保证每个结点平衡因子的绝对值不超过 1，AVL 树的高度就始终能保持 `O(log n)` 级别。由于需要对每个结点都得到平衡因子，因此需要在树的结构中加入一个变量 `height`。

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct Node {
	int v;
	Node* l = nullptr;
	Node* r = nullptr;
	int h = 1;
	Node(int _v) :v(_v) {}
};

int get_height(Node* root) {
	return root ? root->h : 0;
}

int get_balance_factor(Node* root) {
	return get_height(root->l) - get_height(root->r);
}

void update_height(Node* root) {
	root->h = max(get_height(root->l), get_height(root->r)) + 1;
}

void L(Node*& root) {
	Node* temp = root->r;
	root->r = temp->l;
	temp->l = root;
	update_height(root);
	update_height(temp);
	root = temp;
}

void R(Node*& root) {
	Node* temp = root->l;
	root->l = temp->r;
	temp->r = root;
	update_height(root);
	update_height(temp);
	root = temp;
}

void insert(Node*& root, int val) {
	if (!root) {
		root = new Node(val);
		return; // easy to forget
	}
	if (val < root->v) {
		insert(root->l, val);
		update_height(root);
		if (get_balance_factor(root) == 2) {
			if (get_balance_factor(root->l) == 1) {
				R(root);
			}
			else if (get_balance_factor(root->l) == -1) {
				L(root->l);
				R(root);
			}
		}
	}
	else {
		insert(root->r, val);
		update_height(root);
		if (get_balance_factor(root) == -2) {
			if (get_balance_factor(root->r) == -1) {
				L(root);
			}
			else if (get_balance_factor(root->r) == 1) {
				R(root->r);
				L(root);
			}
		}
	}
}

void pre(Node* root) {
	if (!root) {
		return;
	}
	printf("%d ", root->v);
	pre(root->l);
	pre(root->r);
}

int main() {
	Node* root = nullptr;
	for (int i = 1; i < 10; i++) {
		insert(root, i);
	}
	pre(root);  // 4 2 1 3 6 5 8 7 9
	return 0;
}

```

