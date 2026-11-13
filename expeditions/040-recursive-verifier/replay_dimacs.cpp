// Re-read a complete DIMACS stream against one byte per physical variable.
// The counter has no knowledge of the finite field, gates or address layout.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: replay_dimacs assignment.bin < formula.cnf\n";
        return 2;
    }
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::ifstream witness(argv[1], std::ios::binary);
    if (!witness) return 2;
    std::vector<char> bits{std::istreambuf_iterator<char>(witness), {}};
    std::string p, kind;
    int variables;
    std::int64_t declared;
    if (!(std::cin >> p >> kind >> variables >> declared) || p != "p" ||
        kind != "cnf" || variables <= 0 || declared <= 0 ||
        bits.size() != static_cast<std::size_t>(variables) ||
        !std::all_of(bits.begin(), bits.end(), [](char b) { return b == 0 || b == 1; })) {
        std::cerr << "bad DIMACS header or witness\n";
        return 1;
    }
    std::int64_t seen = 0, failed = 0;
    bool satisfied = false;
    int width = 0, lit;
    while (std::cin >> lit) {
        if (lit == 0) {
            if (!width || ++seen > declared) return 1;
            failed += !satisfied;
            satisfied = false;
            width = 0;
            continue;
        }
        if (++width > 3 || lit < -variables || lit > variables) return 1;
        int address = (lit < 0 ? -lit : lit) - 1;
        satisfied |= (bits[address] == (lit > 0));
    }
    if (!std::cin.eof() || seen != declared || width != 0) return 1;
    std::cout << variables << " variables; " << seen << " clauses; "
              << failed << " failed\n";
}
