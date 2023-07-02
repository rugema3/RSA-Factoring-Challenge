#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <gmp.h>

// Pollard's rho algorithm for integer factorization
void factorize_number(const mpz_t n) {
    mpz_t x, y, d;
    mpz_inits(x, y, d, NULL);

    mpz_set_ui(x, 2);
    mpz_set_ui(y, 2);

    uint64_t i = 1;
    uint64_t k = 2;

    while (i < k) {
        mpz_mul(x, x, x);
        mpz_add_ui(x, x, 1);
        mpz_mod(x, x, n);

        mpz_mul(y, y, y);
        mpz_add_ui(y, y, 1);
        mpz_mod(y, y, n);

        mpz_sub(d, x, y);
        mpz_abs(d, d);

        mpz_gcd(d, d, n);

        if (mpz_cmp_ui(d, 1) != 0 && mpz_cmp(d, n) != 0) {
            mpz_t q;
            mpz_init(q);

            mpz_fdiv_q(q, n, d);

            gmp_printf("%Zd=%Zd*%Zd\n", n, d, q);

            mpz_clear(q);
            break;
        }

        if (i == k) {
            mpz_set(y, x);
            k <<= 1;
        }

        i++;
    }

    mpz_clears(x, y, d, NULL);
}

// Factorize numbers from a file
void factorize_file(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Failed to open file.\n");
        return;
    }

    char* line = NULL;
    size_t len = 0;

    while (getline(&line, &len, file) != -1) {
        mpz_t number;
        mpz_init(number);

        mpz_set_str(number, line, 10);

        factorize_number(number);

        mpz_clear(number);
    }

    free(line);
    fclose(file);
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: ./factors <filename>\n");
        return 1;
    }

    const char* filename = argv[1];
    factorize_file(filename);

    return 0;
}


