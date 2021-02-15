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
#define lv vector<long long>

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
lv q;

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

void blockmax(ll d, ll *x, ll *ans, ll n) {
    // d is the block size
    // x[] is an array of size n
    // the answer is returned in an array ans[] of size at least n-d+1
    // Source: https://contest.cs.cmu.edu/295/f20/lectures/blockmin.txt

    int q1 = 0, q2 = 0;

    for (int i = 0; i < n; i++) {
        while (q1 > q2 && x[q[q1 - 1]] <= x[i]) q1--;
        q[q1++] = i;

        if (i >= d && q[q2] == i - d) q2++;

        if (i >= d-1) {
            ans[i-(d-1)] = x[q[q2]];
        }
    }
}

void solve() {
    ll n, k;
    cin >> n >> k;

    lv cata(n);

    for (ll i = 0; i < n; i++) {
        cata[i] = n-i;
    }

    ll cur_pos = 0;

    // if (k == 1) {
    //     cout<<cur_pos<<"\n";
    //     return;
    // }

    for (ll i = 0; i < k; i++) {
        ll cata_ind = i % n;
        cur_pos++;
        if (cur_pos > n) {
            cur_pos -= n;
        }
        if (cata[cata_ind] == cur_pos) {
            cur_pos++;
            if (cur_pos > n) {
                cur_pos -= n;
            }
        }
        cout<<"cur_pos: "<<cur_pos<<" ";
    }
    newline;
    cout<<cur_pos<<"\n";
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


