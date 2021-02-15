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
#define ls set<long long>
#define lms multiset<long long>

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

void print_lms(lms s) {
    for (auto it = s.begin(); it != s.end(); it++) {
        // cout<<" "<<*it;
        cout<<*it<<" ";
    }
    newline;
}

void print_ls(ls s) {
    for (auto it = s.begin(); it != s.end(); it++) {
        // cout<<" "<<*it;
        cout<<*it<<" ";
    }
    newline;
}


/* 
 * Generates all the prime factors given n
 * and returns a vector containing them. 
 * This code is from: 
 * https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/.
 */
lms generate_prime_factors(ll n) {
    lms factors;

    while (n % 2 == 0) {
        factors.insert(2);
        n /= 2;
    }

    for (ll i = 3; i <= sqrt(n); i+=2) {

        // while i divides n, add i to the list and divide n
        while (n % i == 0) {
            factors.insert(i);
            n /= i;
        }
    }

    if (n > 2) {
        // this means that n is  aprime greater than 2.
        factors.insert(n);
    }
    return factors;
}

void solve() {
    // write solution here

    ll n, k;
    cin >> n >> k;

    if (k >= n) {
        cout<<1<<"\n";
        return;
    }

    ll max_d = intmin;

    for (ll i = 1; i < sqrt(n)+1; i++) {
        if (n % i == 0) {
            ll d1 = i;
            ll d2 = n/i;
            // cout<<"d1, d2: "<<d1<<" "<<d2<<"\n";
            // cout<<"k: "<<k<<"\n";
            if (d2 > d1 && d2 <= k) {
                if (d2 > max_d) {
                    max_d = d2;
                }
            } else {
                if (d1 <= k) {
                    if (d1 > max_d) {
                        max_d = d1;
                    }
                }
            }
        }
    }

    // cout<<"max d: "<<max_d<<"\n";
    ll result = n/max_d;
    cout<<result<<"\n";
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


