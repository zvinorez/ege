#pragma once
#include <bits/stdc++.h>

// https://inf-ege.sdamgia.ru/problem?id=59707

inline void task() {
    std::cout << "x y z w" << std::endl;
    for (int x = 0; x < 2; ++x) {
        for (int y = 0; y < 2; ++y) {
            for (int z = 0; z < 2; ++z) {
                for (int w = 0; w < 2; ++w) {
                    if ((x || !y) && !(y == z) && !w) {
                        std::cout << x << " " << y << " " << z << " " << w << std::endl;
                    }
                }
            }
        }
    }
}

// Ответ: xzyw
