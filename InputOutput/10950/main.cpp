#include<iostream>
#include<vector>
using namespace std;

int main() {

	int N;
	cin >> N;
	vector<int> answer;
	int A, B;
	for (int i = 0; i < N; i++) {
		cin >> A>> B;
		answer.push_back(A + B);
		cout << answer.back()<<"\n";
		answer.pop_back();
	}
}