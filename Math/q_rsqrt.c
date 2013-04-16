#include "stdio.h"
#include "math.h"
#include "assert.h"

float q_rsqrt(float number) {
  long i;
  float x2, y;
  const float threehalfs = 1.5F;
  x2 = number * 0.5F;
  y = number;
  i = *(long *) &y;
  i = 0x5f3759df - (i>>1);
  y = *(float*) &i;
  y = y * (threehalfs - (x2 * y * y));
  return y;
}


int main() {
  printf("Inverse square root of 5: %f\n", q_rsqrt(5.0));
  printf("Inverse square root of 4.2: %f\n", q_rsqrt(4.2));

  assert(abs(q_rsqrt(5.0) - .44721) < .01);
  assert(abs(q_rsqrt(4.2) - .48795) < .01);

  return 0;
}
