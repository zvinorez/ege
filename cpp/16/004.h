#pragma once
#include <bits/stdc++.h>

// #5157 kompege
// Алгоритм вычисления значения функции F(n) где n – натуральное число, задан следующими соотношениями:
// F(n) = n при n ≤ 3
// F(n) = 2n + F(n − 2) при n > 3 и нечётном n,
// F(n) = n^2 + F(n − 1) при n > 3 и чётном n
// В качестве ответа на задание выведите значение F(10 000) − F(9 995).


inline int f(int n) {
    if (n <= 3) return n;
    if (n % 2 == 1) return 2 * n + f(n - 2);
    return n * n + f(n - 1);
}

inline void task() {
    std::cout << f(10000) - f(9995) << std::endl;
}

// Ответ: 100039992
