#include <stdio.h>

int main()
{
    int n, i, target, found = 0;
    int arr[100]; // Declare an array with a maximum size of 100

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

    // Ask user for the target element to search for
    printf("Enter the target element to search for: ");
    scanf("%d", &target);

    // Perform linear search
    for (i = 0; i < n; i++)
    {
        if (arr[i] == target)
        {
            printf("Element %d found at position %d.\n", target, i + 1);
            found = 1;
            break;
        }
    }

    // If the element is not found
    if (!found)
    {
        printf("Element %d not found in the array.\n", target);
    }

    return 0;
}
