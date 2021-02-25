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

bool is_ramp_number(string s) {
    char prev = s[0];
    for (char c : s) {
        if (c < prev) {
            return false;
        }
        prev = c;
    }
    return true;
}

map<string, ll> mem;

ll solve(string num) {
    // write solution here
    // string num;
    // cin >> num;
    if (!is_ramp_number(num)) {
        return -1;
    }

    ll strlen = num.length();

    if (num.length() == 1) {
        return mem[num];
    } else if (num.back() == '0') {
        string fin = to_string(9);
        ll mid = num.end()[-2] - '0';
        mid--;
        string str_mid = to_string(mid);

        string recurse = num.substr(0, strlen-2) + str_mid + fin;

        ll recurse_result = solve(recurse);
        mem[recurse] = recurse_result;
        mem[num] = recurse_result;
        return recurse_result;
    }

    string last = string(1, num.back());
    ll b = num.end()[-2] - '0';

    // string remain = num.substr(0, strlen-2) + to_string(b-1) + to_string(9);
    string remain = num.substr(0, strlen-1) + to_string(0);
    cout<<"remain: "<<remain<<"\n";

    ll last_num_result = solve(last);
    ll result = last_num_result - b + 1 + solve(remain);

    mem[num] = result;
    mem[remain] = result - last_num_result + b - 1;

    return result;
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1; 
    cin >> tc; // comment out this lnie if only 1 test


    for (ll i = 1; i < 9; i++) {
        mem[to_string(i)] = i;
    }

    for (int t = 1; t <= tc; t++) {
        string num;
        cin >> num;
        ll result = solve(num);
        cout<<result<<"\n";
    }

}

