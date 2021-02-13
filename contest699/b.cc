#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;



void solve() {
    int n, k;
    cin >> n >> k;
    vector<int> mtns;
    int input;
    int last = -1;

    for(int ind = 0; ind < n; ind++) {
        cin >> input;
        mtns.push_back(input);
    }

    int i = 0;
    while (k--) {

        if (i > 0 && mtns[i-1] < mtns[i]) {
            i--;
        }

        while (i < n-1 && mtns[i] >= mtns[i+1]) {
            i++;
        }

        if (i == n-1) {
            // last = -1;
            // continue;
            cout << -1 << "\n";
            return;
        }

        if (i < n-1) {
            mtns[i] += 1;
            last = i;
        }
    }

    if (last == -1) {
        cout << last << "\n";
    } else {
        cout << last+1 << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        solve();
    }
}