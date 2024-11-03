#include <stdio.h>

int main()
{
    int n, target, left, right, mid;
    int found = 0;
    int arr[100]; // Declare an array with a maximum size of 100

    // Ask user for the number of elements
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    // Input elements of the array
    printf("Enter the elements of the array in sorted order:\n");
    for (int i = 0; i < n; i++)
    {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Ask user for the target element to search for
    printf("Enter the target element to search for: ");
    scanf("%d", &target);

    // Initialize left and right pointers
    left = 0;
    right = n - 1;

    // Perform binary search
    while (left <= right)
    {
        mid = left + (right - left) / 2;

        // Check if target is present at mid
        if (arr[mid] == target)
        {
            printf("Element %d found at position %d.\n", target, mid + 1);
            found = 1;
            break;
        }

        // If target is greater, ignore left half
        if (arr[mid] < target)
        {
            left = mid + 1;
        }
        // If target is smaller, ignore right half
        else
        {
            right = mid - 1;
        }
    }

    // If target is not found
    if (!found)
    {
        printf("Element %d not found in the array.\n", target);
    }

    return 0;
}
