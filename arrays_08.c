#include <stdio.h>

int main()
{
    int n, i;
    int even = 0, odd = 0; // Initialize counters for even and odd numbers
    int arr[100];          // Declare an array with a maximum size of 100

    // Ask user for the number of elements
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    // Input elements of the array
    printf("Enter the elements of the array:\n");
    for (i = 0; i < n; i++)
    {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Count even and odd numbers
    for (i = 0; i < n; i++)
    {
        if (arr[i] % 2 == 0)
        {
            even++;
        }
        else
        {
            odd++;
        }
    }

    // Print the count of even and odd numbers
    printf("Number of even numbers: %d\n", even);
    printf("Number of odd numbers: %d\n", odd);

    return 0;
}
