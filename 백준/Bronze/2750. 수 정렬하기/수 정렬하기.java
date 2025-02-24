import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int n = Integer.parseInt(sc.nextLine());
        int[] arr = new int[n];
        for(int i=0; i< n; i++){
            arr[i] = Integer.parseInt(sc.nextLine());
        }
        
        bubble_sort(arr);
        for (int i =0; i < n; i++){
            System.out.println(arr[i]);
        }
    }
    public static void bubble_sort(int arr[]){
        
        for(int i=1; i < arr.length; i++){
            for(int j = 0; j < arr.length - i; j++){
                if(arr[j] > arr[j+1]){
                    swap(arr, j, j+1);
                }
            }
        }
    }
    
    public static void swap(int arr[], int a, int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}