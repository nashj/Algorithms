#include<math.h>

float Q_rsqrt(float number) {
  long i;
  float x2, y;
  const float threehalfs = 1.5F;
  x2 = number * 0.5F;
  y = number;

  // Cast the floating point number into an integer
  i = *(long*) &y;
  // This is the famous and tricky step: 
  // If you have a number like 10^6, the 
  // square root is given by dividing the exponent by two,
  // so the square root of 10^6 is 10^3.
  // For the inverse square root, you divide by -2 to get 10^-3.
  // Since floating point is represented as:
  // sign - exponent - mantissa
  // shifting by two divides the exponent by two. 
  // Subtracting the exponent from zero results in the negative exponent. 
  // The magic number also takes care of other things like the mantissa
  i = 0x5f3759df - (i>>1);
  // Recast the number back into floating point
  y = *(float*) &i;
  // Perform one iteration of Newton's method
  // This formula comes from the standard Newton's method update step:
  // new_guess = guess - f(guess) / f'(guess)
  // In this case, f(guess) = 1/guess^2 - number 
  // Therefore, f'(guess) = -2*guess^-3
  // Together, that's:
  // guess = guess + guess/2 - number*.5*guess^3, which is simplified to:
  y = y*(threehalfs-(x2*y*y));
  return y;
}

int main() {
  printf("Q_rsqrt: %f\n", Q_rsqrt(5));
  printf("Math 1/sqrt: %f\n", 1/sqrt(5));

  return 0;
}
