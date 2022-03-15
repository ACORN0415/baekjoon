#include<iostream>
#include<vector>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	vector<int> answer;
	int A, B;
	for (int i = 0; i < T; i++) {
		cin >> A >> B;
		answer.push_back(A + B);
		cout << answer.back() << "\n";
		answer.pop_back();
	}
	
}
	