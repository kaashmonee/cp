#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long
#define for_range(s, e, inc) for (ll i = 0; i < e; i+=inc)

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ll template_array_size = 1e6 + 4265;
ll a[template_array_size];
ll b[template_array_size];
ll c[template_array_size];

// string s, t;
ll ans = 0;


void solve() {
    // write solution here
    int n, k;
    string s;
    // vector<string> letters;
    unordered_set <char> letters;
    cin >> n >> k;
    cin >> s;
    int ktemp = k;

    while (ktemp--) {
        char l;
        cin >> l;
        letters.insert(l);
    }


    ll f[n+1];
    f[0] = 0;

    for (ll i = 1; i < n+1; i++) {

        if (letters.find(s[i-1]) != letters.end()) {
            f[i] = f[i-1] + 1;
        } else {
            f[i] = 0;
        }

    }

    ll sum = 0;
    for (auto i : f) {
        sum += i;
    }
    cout<<sum<<"\n";

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


