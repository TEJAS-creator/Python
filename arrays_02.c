#include <stdio.h>

int main()
{
    int n, i, largest; // Declare variables at the beginning
    int arr[100];      // Declare array with a maximum size

    // Ask user for the number of elements
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    // Input elements of the array
    printf("Enter the elements of the array:\n");
    for (i = 0; i < n; i++)
    {
        printf("Element %d: ", i++);
        scanf("%d", &arr[i]);
    }

    // Initialize the largest variable with the first element
    largest = arr[0];

    // Traverse the array to find the largest element
    for (i = 1; i < n; i++)
    {
        if (arr[i] > largest)
        {
            largest = arr[i];
        }
    }

    // Print the largest element
    printf("The largest element in the array is: %d\n", largest);
    return 0;
}
