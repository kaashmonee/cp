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
#define N 10000

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;

// this is just some random thing that i guess you could use in the template
ll q[N] = {0};


void blockmax(ll d, ll *x, ll *ans, ll n) {
    // d is the block size
    // x[] is an array of size n
    // the answer is returned in an array ans[] of size at least n-d+1

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
    ll n;
    cin >> n;
    ll ntemp = n;

    ll x[n] = {0};

    for (ll i = 0; i < n; i++) {
        ll si;
        cin >> si;
        x[i] = si;
    }

    ll ans[N] = {0};

}

// Example usage
// int main() {
//     int x[] = {1,2,3,4,3,2,1};
//     n = 7;
//     int d = 3;
//     blockmin (d, x, ans);
//     for (int i=0; i<n-d+1; i++) {
// 	printf("%d ", ans[i]);
//     }
//     printf("\n");
//     return 0;
// }


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1; 
    // cin >> tc; // comment out this lnie if only 1 test
    for (int t = 1; t <= tc; t++) {
        solve();
    }

}


