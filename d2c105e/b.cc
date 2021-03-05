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

bool berland(ll n, lm &d, lm &c, ll i) {

    if (d == c) return true;

    for (ll k = 0; k < 4; k++) {
         
    }

    cout<<"d:\n";
    print_lm(d);
    newline;

    cout<<"c:\n";
    print_lm(c);
    newline;

    for (ll ind = i; ind < 4; ind++) {
        // place in first corner
        // cout<<"ind: "<<ind<<"\n";
        // if (d[i] < 0) return false;

        c[(ind+1)%4]++;
        d[(ind+1)%4]--;
        if (d[ind] == n) {
            c[(ind-1+4)%4]++;
            d[(ind+1)%4]--;
        }
        ll result = berland(n, d, c, ind+1);

        if (result) return true;

        if (d[ind] != n) {
            c[(ind+1)%4]--;
            c[(ind-1+4)%4]++;
            d[(ind+1)%4]++;
            d[(ind-1+4)%4]--;

            result = berland(n, d, c, ind+1);

            if (result) return true;

            if (d[ind] == n-1) {
                return false;
            }

            c[(ind+1)%4]++;
            c[(ind-1+4)%4]--;
            d[(ind+1)%4]--;
            d[(ind-1+4)%4]++;

            result = berland(n, d, c, ind+1);
            if (result) return true;

        } else {
            return false;
        }
    }


    return false;
}

void solve() {
    ll n, u, r, d, l;
    cin >> n >> u >> r >> d >> l;

    if (u > n || r > n || d > n || l > n) {
        cout<<"NO\n";
        return;
    }

    lm de;
    de[0] = u;
    de[1] = r;
    de[2] = d;
    de[3] = l;

    lm c;
    c[0] = 0;
    c[1] = 0;
    c[2] = 0;
    c[3] = 0;

    lm rem;
    rem[0] = u;
    rem[1] = r;
    rem[2] = d;
    rem[3] = l;

    bool result = berland(n, de, c, 0);
    if (result) cout<<"YES\n";
    else cout<<"NO\n";
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


