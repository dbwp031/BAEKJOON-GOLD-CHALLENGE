#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	int arr[1005][3];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 3; j++) { 
			cin>>arr[i][j];
		}
	}
	int result[1005][3];
	result[0][0] = arr[0][0];
	result[0][1] = arr[0][1];
	result[0][2] = arr[0][2];
    
	for (int i = 1; i < n; i++) {
		result[i][0] = min(result[i - 1][1], result[i - 1][2]) + arr[i][0];
		result[i][1] = min(result[i - 1][0], result[i - 1][2]) + arr[i][1];
		result[i][2] = min(result[i - 1][1], result[i - 1][0]) + arr[i][2];
	}
	cout << min(min(result[n - 1][0], result[n - 1][1]), result[n - 1][2]);
	return 0;
}
