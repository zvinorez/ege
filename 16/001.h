#pragma once
#include <bits/stdc++.h>

// #10 kompege
// Алгоритм вычисления значения функции F(n) где n – натуральное число, задан следующими соотношениями:
// F(0) = 1, F(1) = 3, F(2)=2,  F(n) = F(n−1) * F(n−3) при n > 2 Чему равно значение функции F(7)?
// В ответе запишите только целое число.


inline int f(int n) {
    if (n == 0) return 1;
    if (n == 1) return 3;
    if (n == 2) return 2;
    return f(n - 1) * f(n - 3);
}

inline void task() {
    std::cout << f(7) << std::endl;
}
// Ответ: 144
