#include <stdio.h>

int main()
{
    int n, i;
    int arr1[100], arr2[100], sum[100]; // Declare arrays with a maximum size of 100

    // Ask user for the number of elements
    printf("Enter the number of elements in the arrays: ");
    scanf("%d", &n);

    // Input elements of the first array
    printf("Enter the elements of the first array:\n");
    for (i = 0; i < n; i++)
    {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr1[i]);
    }

    // Input elements of the second array
    printf("Enter the elements of the second array:\n");
    for (i = 0; i < n; i++)
    {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr2[i]);
    }

    // Add the elements of both arrays
    for (i = 0; i < n; i++)
    {
        sum[i] = arr1[i] + arr2[i];
    }

    // Print the resulting array
    printf("The resulting array after addition is:\n");
    for (i = 0; i < n; i++)
    {
        printf("%d ", sum[i]);
    }
    printf("\n");

    return 0;
}
