#include <stdio.h>
#include <assert.h>

void swap(char *a, char *b) {
  char d = *a;
  *a = *b;
  *b = d;
}

void reverse_inplace(char *str) {
  // Modifies str

  // Determine length O(n)
  char *idx = str;
  while (*idx) idx++;
  int length = idx - str;

  // Swap elements in place O(n)
  for (int i = 0; i < length/2; i++) {
    swap(&str[i], &str[length-1-i]);
  }

}

int str_cmp(char *a, char *b) {
  int i;
  for (i = 0; *(a+i); i++) {
    if (a[i] != b[i]) return 0;
    //assert(a[i] == b[i]);
  }
  if (*(b+i)) return 0; 
  return 1;
}

int main() {
  char str1[] = "Test test test";
  char str2[] = "Gutenberg";
  char str3[] = "Gutenbergs";

  char rev_str1[] = "tset tset tseT"; //Test test test";
  char rev_str2[] = "grebnetuG"; //Gutenberg";
  char rev_str3[] = "sgrebnetuG"; //Gutenbergs";

  reverse_inplace(str1);
  reverse_inplace(str2);
  reverse_inplace(str3);

  assert(str_cmp(str1, rev_str1));
  assert(str_cmp(str2, rev_str2));
  assert(str_cmp(str3, rev_str3));
}
