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
#define lv vector<long long>

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;

// this is just some random thing that i guess you could use in the template
ll q[N] = {0};


// void blockmax(ll d, ll *x, ll *ans, ll n) {
//     // d is the block size
//     // x[] is an array of size n
//     // the answer is returned in an array ans[] of size at least n-d+1

//     int q1 = 0, q2 = 0;

//     for (int i = 0; i < n; i++) {
//         while (q1 > q2 && x[q[q1 - 1]] <= x[i]) q1--;
//         q[q1++] = i;

//         // if i and i - d are at the same location
//         if (i >= d && q[q2] == i - d) q2++;

//         if (i >= d-1) {
//             ans[i-(d-1)] = x[q[q2]];
//         }
//     }
// }

auto my_blockmax(vector<ll> inp, ll n) {
    vector<ll> left(n);
    vector<ll> right(n);

    stack<ll> sleft;
    stack<ll> sright;

    for (ll i=0; i<n; i++) {
        while (sleft.size() > 0 && sleft.top() <= inp[i]) {
            sleft.pop();
        }

        if (sleft.size() == 0) {
            left[i] = -1;
        } else {
            left[i] = sleft.top();
        }

        sleft.push(inp[i]);
    }

    for (ll i = n-1; i >= 0; i--) {
        while (sright.size() > 0 && sright.top() <= inp[i]) {
            sright.pop();
        }

        if (sright.size() == 0) {
            right[i] = -1;
        } else {
            right[i] = sright.top();
        }

        sright.push(inp[i]);
    }

    pair<vector<ll>, vector<ll>> p = {left, right};
    return p;
}

void solve() {
    ll n;
    cin >> n;

    vector<ll> x;

    for (ll i = 0; i < n; i++) {
        ll si;
        cin >> si;
        x.push_back(si);
    }
    if (n == 1) {
        cout<<x[0]<<"\n";
        return;
    }

    auto result = my_blockmax(x, n);
    lv left = result.first;
    lv right = result.second;

    // print_list(left);
    // newline;
    // print_list(right);
    // newline;

    ll max_xor = 0;

    for (ll i = 0; i < n; i++) {
        ll snd_max = x[i];
        ll max_num = max(left[i], right[i]);

        ll lucky_num = snd_max ^ max_num;
        if (lucky_num > max_xor) {
            max_xor = lucky_num;
        } 
    }

    cout<<max_xor<<"\n";

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


