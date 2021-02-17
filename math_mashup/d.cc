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
 * Also added a mem parameter for memoization.
 */
// lv generate_prime_factors(ll n, map<ll, lv> mem) {
//     lv factors;

//     while (n % 2 == 0) {
//         if (mem.find(n) != mem.end()) {
//             // if we find the result in the memtable, then we retrieve
//             // the memoized result
//             factors.insert(factors.end(), mem[n].begin(), mem[n].end());
//             return factors;
//         } 
//         factors.push_back(2);
//         n /= 2;
//     }

//     for (ll i = 3; i <= sqrt(n); i+=2) {

//         // while i divides n, add i to the list and divide n
//         while (n % i == 0) {

//             if (mem.find(n) != mem.end()) {
//                 // if we find the result in the memtable, then we retrieve 
//                 // the memoized result
//                 factors.insert(factors.end(), mem[n].begin(), mem[n].end());
//                 return factors;
//             } 

//             factors.push_back(i);
//             n /= i;

//         }
//     }

//     if (n > 2) {
//         // this means that n is  aprime greater than 2.
//         factors.push_back(n);
//     }

//     return factors;
// }

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

// modular exponent function taken from:
// CP handbook
ll modpow(ll x, ll n, ll m) {
    if (n == 0) 
        return 1%m;

    ll u = modpow(x,n/2,m);

    u = (u*u)%m;

    if (n%2 == 1) u = (u*x)%m;
    
    return u;
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

ll g(ll x, ll p) {
    // computes g
    ll pk = p;
    ll max_pk = intmin;

    if (x % p != 0) {
        return 1;
    }

    while (pk <= x) {
        if (x % pk == 0 && pk > max_pk) {
            max_pk = pk;
        }

        pk *= p;
    }

    return max_pk;
}

ll f(lm primes, ll y) {
    ll result = 1;
    for (auto prime : primes) {
        result = (result * g(y, prime.first)) % MOD;
    }
    return result % MOD;
}

/*
void solve() {
    // write solution here

    ll x, n;
    cin >> x >> n;

    auto primes = generate_prime_factors(x); 
    
    ll prod = 1;

    // This is probably where i have to optimize it
    // i think i need to do some fun DP type stuff here
    // specifically, i think some relationship between f(primes, i) 
    // would be great with each other
    for (ll z = 1; z <= n; z++) {

        auto zprimes = generate_prime_factors(z);

        for (auto pzi : zprimes) {
            prod *= f(zprimes, pzi.first) % MOD;
        }

        // prod *= (f(primes, z));
        // prod = prod % MOD;
    }
    
    prod = prod % MOD;
    cout<<prod<<"\n";
}
*/

ll h(ll n, ll p) {
    ll k = 1;
    ll sum = 0;
    ll val = 1;

    while (val > 0) {
        val = floor(n/(pow(p, k)));
        sum += val;
        k++;
        // cout<<"val: "<<val<<"\n";
    }
    // cout<<"sum: "<<sum<<"\n";
    return sum;
}

void solve() {
    ll x, n;
    cin >> x >> n;
    cout<<"n: "<<n<<"\n";

    auto primes = generate_prime_factors(x);
    print_lm(primes);

    ll prod = 1;
    for (auto p : primes) {
        unsigned long long hn = (unsigned long long) h(n, p.first);
        prod *= (modpow(p.first, hn, MOD) % MOD) % MOD;
        cout<<"hn: "<<hn<<"\n";
        cout<<"hnmod: "<<hn % (MOD)<<"\n";
        cout<<"prod: "<<prod<<"\n";
        cout<<"modpow: "<<modpow(p.first, hn, MOD)<<"\n";
    }

    cout<<prod % MOD<<"\n";

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

