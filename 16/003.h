#pragma once
#include <bits/stdc++.h>

// #597 kompege
// Алгоритм вычисления значения функции F(n) где n – натуральное число, задан следующими соотношениями:
// F(n) = n при n ≤ 10
// F(n) = n // 4 + F(n - 10) если 10 < n ≤ 36,
// F(n) = 2 * F(n - 5) если n > 36
// Здесь // обозначает деление нацело. В качестве ответа на задание выведите значение F(100).


int f(int n) {
    if (n <= 10) return n;
    if (n > 10 && n <= 36) return n / 4 + f(n - 10);
    return 2 * f(n - 5);
}

inline void task() {
    std::cout << f(100) << std::endl;
}

// Ответ: 180224