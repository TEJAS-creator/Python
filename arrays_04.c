#include <stdio.h>

int main()
{
    int n, i, sum = 0;
    int arr[100];

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

    // Calculate the sum of all elements
    for (i = 0; i < n; i++)
    {
        sum = sum + arr[i];
    }

    // Print the sum of the elements
    printf("The sum of all elements in the array is: %d\n", sum);

    return 0;
}
