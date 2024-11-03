#include <stdio.h>

int main()
{
    int arr[100], n, i, pos, element;

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

    // Ask user for the position and element to insert
    printf("Enter the position where you want to insert the element: ");
    scanf("%d", &pos);

    printf("Enter the element to insert: ");
    scanf("%d", &element);

    // Check if the position is valid
    if (pos < 1 || pos > n + 1)
    {
        printf("Invalid position! Please enter a position between 1 and %d\n", n + 1);
    }
    else
    {
        // Shift elements to the right
        for (i = n; i >= pos; i--)
        {
            arr[i] = arr[i - 1];
        }

        // Insert the element at the specified position
        arr[pos - 1] = element;

        // Increment the number of elements
        n++;

        // Print the updated array
        printf("Array after insertion:\n");
        for (i = 0; i < n; i++)
        {
            printf("%d ", arr[i]);
        }
        printf("\n");
    }

    return 0;
}
