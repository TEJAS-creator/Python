#include <stdio.h>

int main()
{
    int n, i;
    float sum = 0.0, average; // Declare sum as float to handle decimal values
    int arr[100];             // Declare an array with a maximum size of 100

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
        sum += arr[i];
    }

    // Calculate the average
    average = sum / n;

    // Print the sun of the elements
    printf("The sum of all elements in the array is: %.2f\n", sum);

    // Print the average of the elements
    printf("The average of all elements in the array is: %.2f\n", average);

    return 0;
}
