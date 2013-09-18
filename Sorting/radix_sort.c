#include "stdio.h"
#include "stdlib.h"
#include "math.h"

int nth_digit(int x, int n) {
  while (n--) {
    x /= 10;
  }
  return (x % 10);
}

void print_list(int * list, int list_size) {
  int i;
  for (i = 0; i < list_size; i++) {
    printf("%d ", list[i]);
  }
  printf("\n\n");
}

void radix_sort(int * list, int list_size) {
  // Note: modifies list

  // find maximum elements
  int i;
  int k;
  int range = 10;
  int max = 0;
  for (i = 0; i < list_size; i++) {
    if (list[i] > max) {
      max = list[i];
    }
  }
  int max_digits = floor(log10(max) + 1);

  // allocate a second list that is the length of the original
  int *sorted_list = (int *) malloc(sizeof(int) * list_size);
  // allocate a third list that is the length of the original
  int counter_list[10] = {0}; 

  for (k = 0; k < max_digits; k++) {
    // Zero both lists
    for (i = 0; i < range; i++) {
      counter_list[i] = 0;
    }

    // Populate counter list and zero sorted_list
    for (i = 0; i < list_size; i++) {
      sorted_list[i] = 0;
      counter_list[ nth_digit(list[i],k) ]++; 
    }

    for (i = 1; i < range; i++) {
      counter_list[i] = counter_list[i] + counter_list[i-1];
    }

    for (i = 0; i < range; i++) {
      counter_list[i]--;
    }

    for (i = list_size-1; i >= 0; i--) {
      sorted_list[ counter_list[ nth_digit(list[i],k) ] ] = list[i];
      counter_list[ nth_digit(list[i],k) ]--; 
    }

    for (i = 0; i < list_size; i++) {
      list[i] = sorted_list[i]; 
    }
  }

  free(sorted_list);
}

int main() {
  int list[] = {435,1432,6456,23432,732,234,6546,234,76571,123};
  print_list(list, 10);
  radix_sort(list, 10);
  print_list(list, 10);
  return 0;

}
