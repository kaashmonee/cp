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
#define lm map<long, long>

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


/* 
 * Generates all the prime factors given n
 * and returns a vector containing them. 
 * This code is from: 
 * https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/.
 */
lm generate_prime_factors(ll n) {
    lm factors;

    while (n % 2 == 0) {
        if (factors.find(2) != factors.end()) {
            factors[2]++;
        } else {
            factors[2] = 1;
        }
        n /= 2;
    }

    for (ll i = 3; i <= sqrt(n); i+=2) {

        // while i divides n, add i to the list and divide n
        while (n % i == 0) {
            if (factors.find(i) != factors.end()) {
                factors[i]++;
            } else {
                factors[i] = 1;
            }
            n /= i;
        }
    }

    if (n > 2) {
        // this means that n is  aprime greater than 2.
        factors[n] = 1;
    }

    return factors;
}

// Computes the euler totient function
// The euler totient function counts the number of integers that are coprime
// from 1 to n.
ll totient(ll n) {
    lm primes = generate_prime_factors(n);

    ll t = 1;
    for (auto p : primes) {
        t *= (ll) powl(p.first, p.second-1) * (p.first-1);
    }

    return t;
}

void print_lms(lms s) {
    for (auto it = s.begin(); it != s.end(); it++) {
        cout<<*it<<" ";
    }
    newline;
}

void print_ls(ls s) {
    for (auto it = s.begin(); it != s.end(); it++) {
        cout<<*it<<" ";
    }
    newline;
}

void print_lm(lm m) {
    for (auto e : m) {
        cout<<"K: "<<e.first<<" V: "<<e.second<<"\n";
    }
    newline;
}

// modular exponent function taken from:
// CP handbook
ll modpow(ll x, ll n, ll m) {
    if (n == 0) 
        return 1%m;

    ll u = modpow(x,n/2,m);

    u = (u*u)%m;
    // cout<<"u: "<<u<<"\n";

    if (n%2 == 1) u = (u*x)%m;
    
    return u;
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

// just have to write this function
bool suff(string s, ll ind, vector<vector<ll>> &dat) {
    return true;
}

void solve() {
    // write solution here
    ll n, k;
    cin >> n >> k;

    string s;
    cin >> s;

    if (n % k != 0) {
        cout<<-1<<"\n";
        return;
    }

    // contains the prefix counts of each letter in the string 
    // up until a particular index
    vector<vector<ll>> dat(26, vector<ll>(n, 0));

    for (ll i = 0; i < n; i++) {
        ll c = (ll) s[i] - 'a';
        for (ll j = 1; j < 26; j++) {
            dat[i][j] = dat[i][j-1];
        }
        dat[i][c]++;
    }

    // represents the start of the suffix
    // since we're binary searching, we start it at n/2
    ll start, end, mid;
    start = 0; 
    end = n;
    mid = n/2;

    while (start < end-1) {

        bool works = suff(s, mid, dat);
        
        if (works) {
            mid += mid/2;
            start = mid;
        } else {
            mid -= mid/2;
            end = mid;
        }
    }


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


