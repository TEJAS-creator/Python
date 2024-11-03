#include <stdio.h>

int main()
{
    int n, i, smallest; // Declare variables at the beginning
    int arr[100];       // Declare array with a maximum size

    // Ask user for the number of elements
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    // Input elements of the array
    printf("Enter the elements of the array:\n");
    for (i = 0; i < n; i++)
    {
        printf("Element %d: ", i);
        scanf("%d", &arr[i]);
    }

    // Initialize the smallest variable with the first element
    smallest = arr[0];

    // Traverse the array to find the smallest element
    for (i = 1; i < n; i++)
    {
        if (arr[i] < smallest)
        {
            smallest = arr[i];
        }
    }

    // Print the smallest element
    printf("The smallest element in the array is: %d\n", smallest);
    return 0;
}
