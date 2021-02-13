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

void solve() {
    // write solution here
    ll ntemp;
    cin >> ntemp;
    ll n = ntemp;

    vector<array<ll, 2>> intvls;

    while (ntemp--) {
        ll s, e;
        cin >> s >> e;
        intvls.push_back({s, e});
    }

    // sorts based on the first element
    srtfn(intvls, [](auto a, auto b) {return a[0] < b[0];});

    map<ll, ll> max_map;

    for (auto intvl : intvls) {
        ll s, e;
        s = intvl[0];
        e = intvl[1];

        // fond it
        if (max_map.find(s) != max_map.end()) {
            if (e > max_map[s]) {
                max_map[s] = e;
            }
        } else {
            // didn't find it, inserting the element
            max_map[s] = e;
        }
    }

    ll covered = 0;
    ll cur_max = intmin;

    for (ll i = 0; i < n; i++) {
        ll s, e;
        s = intvls[i][0];
        e = intvls[i][1];

        if (e > cur_max) {
            cur_max = e;
        } else {
            covered++;
        }
    }

    cout<<covered<<"\n";

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


