#include <stdio.h>

int main()
{
    int arr[100], n, i, pos;

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

    // Ask user for the position to delete
    printf("Enter the position where you want to delete the element: ");
    scanf("%d", &pos);

    // Check if the position is valid
    if (pos < 1 || pos > n)
    {
        printf("Invalid position! Please enter a position between 1 and %d\n", n);
    }
    else
    {
        // Shift elements to the left
        for (i = pos - 1; i < n - 1; i++)
        {
            arr[i] = arr[i + 1];
        }

        // Decrement the number of elements
        n--;

        // Print the updated array
        printf("Array after deletion:\n");
        for (i = 0; i < n; i++)
        {
            printf("%d ", arr[i]);
        }
        printf("\n");
    }

    return 0;
}
