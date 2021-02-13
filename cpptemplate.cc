#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long
#define newline cout<<"\n"
#define print_list(L) for (auto c : L) {cout<<c<<" ";}
#define printl2d(L) for (auto c : L) {for (auto k : c) {cout<<k<<" ";} cout<<"\n";}
#define srt(L) sort(begin(L), end(L))
#define srtfn(L, fn) sort(begin(L), end(L), fn)
#define intmin LLONG_MIN
#define intmax LLONG_MAX

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;


// log n algorithm to compute the log of some number a with base b
// this function exists to avoid rounding errors with floats
ll compute_log(ll a, ll b) {
    ll ctr = 0;
    if (b == 1) {
        return intmax;
    }
    while (a > 0) {
        a /= b;
        ctr++;
    }
    return ctr;
}

void solve() {
    // write solution here
}



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1; 
    cin >> tc; // comment out this lnie if only 1 test
    for (int t = 1; t <= tc; t++) {
        solve();
    }

}


