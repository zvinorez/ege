#pragma once
#include <bits/stdc++.h>

// №984 kompege

inline void task() {
    auto b = 500 * pow(2, 13) / (10 * pow(2, 10));
    auto a = 500 * pow(2, 13) / (100 * pow(2, 10)) * 2 + 40;
    std::cout << b << " " << a << std::endl;
    std::cout << b - a;
}

// Ответ: А280
