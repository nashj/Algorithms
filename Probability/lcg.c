#include "stdlib.h"
#include "stdio.h"
#include "assert.h"

long int seed = 1;

unsigned int lcg() {
  unsigned int a = 16807;
  unsigned int m = 2147483647; // 2^31 - 1
  seed = (a*seed) % m;
  return seed;
}

int main() {
  int i;
  for (i = 0; i < 100000; ++i) {
    unsigned int r = rand();
    printf("%d: %d\n", i, r);
    assert(r == lcg());
  }
  printf("Tests passed.\n");
  return 0;
}
