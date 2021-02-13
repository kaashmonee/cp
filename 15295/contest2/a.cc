#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long
#define newline cout<<"\n"
#define print_list(L) for (auto c : L) {cout<<c<<" ";}

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;

void solve() {
    // write solution here
    string input;
    cin >> input;

    long double s, e;
    s = 0;
    e = 1e9;

    vector<int> idxs(input.length());
    iota(begin(idxs), end(idxs), 1);
    vector<float> rocks;

    for (char c : input) {
        long double rock_loc = (e+s)/2;
        if (c == 'l') {
            e -= (e-s)/2;
        } else if (c == 'r') {
            s += (e-s)/2; 
        } 

        rocks.push_back(rock_loc);
    }

    // print_list(rocks);
    // newline;

    sort(idxs.begin(), idxs.end(), [rocks](size_t i1, size_t i2) {return rocks[i1-1] < rocks[i2-1];});

    for (auto x : idxs) {
        cout<<x<<"\n";
    }    

}



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1; 
    // cin >> tc; // comment out this lnie if only 1 test
    for (int t = 1; t <= tc; t++) {
        solve();
    }

}


