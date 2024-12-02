#pragma once
#include <bits/stdc++.h>

// https://inf-ege.sdamgia.ru/problem?id=14688

inline void task() {
    std::cout << "x y z" << std::endl;
    for (int x = 0; x < 2; ++x) {
        for (int y = 0; y < 2; ++y) {
            for (int z = 0; z < 2; ++z) {
                if (!((x || y) <= (z == x))) {
                    std::cout << x << " " << y << " " << z << std::endl;
                }
            }
        }
    }
}

// Ответ: xzy
