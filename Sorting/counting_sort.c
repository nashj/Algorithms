#include "stdio.h"
#include "stdlib.h"
#include "math.h"

void print_list(int * list, int list_size) {
  int i;
  for (i = 0; i < list_size; i++) {
    printf("%d ", list[i]);
  }
  printf("\n\n");
}

void counting_sort(int * list, int list_size, int range) {
  // Note: modifies list

  int i;
  // allocate a second list to write the sorted list
  int *sorted_list = (int *) malloc(sizeof(int) * list_size);
  // allocate a third list for counting the occurence of each number in the list
  int *counter_list = (int *) malloc(sizeof(int) * range);

  // Zero both lists
  for (i = 0; i < range; i++) {
    counter_list[i] = 0;
  }
  for (i = 0; i < list_size; i++) {
    sorted_list[i] = 0;
    counter_list[ list[i] ]++; 
  }

  for (i = 1; i < range; i++) {
    counter_list[i] = counter_list[i] + counter_list[i-1];
  }

  for (i = 0; i < range; i++) {
    counter_list[i]--;
  }
  
  for (i = list_size-1; i >= 0; i--) {
    sorted_list[ counter_list[list[i]] ] = list[i];
    counter_list[list[i]]--; 
  }

  for (i = 0; i < list_size; i++) {
    list[i] = sorted_list[i]; 
  }
  
  free(sorted_list);
  free(counter_list);
}

int main() {
  int list[] = {4,5,6,7,2,3,5,6,7,8,0,9,9,9,9,9,9,9,7,6,2,3,4,5,6,1,1,3,4,5,6,7,4,3,2,3,5,6,7,4,3,2,3,4,5,6,6,1,1,1,1,2,3,5,4,3,2,3,3,4,4,5,6};
  print_list(list, 63);
  counting_sort(list, 63, 10);
  print_list(list, 63);
}

