import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int n = Integer.parseInt(sc.nextLine());
        int[] arr = new int[n];
        for(int i=0; i< n; i++){
            arr[i] = Integer.parseInt(sc.nextLine());
        }
        
        selection_sort(arr);
        for (int i =0; i < n; i++){
            System.out.println(arr[i]);
        }
    }

    
    public static void selection_sort(int arr[]) {
    	int min_idx = 0;
    	for (int i = 0; i < arr.length; i++) {
    		for(int j = i + 1; j < arr.length; j++) {
    			if (arr[j] < arr[min_idx]) {
    				swap(arr,min_idx, j);
    			}
    		}
    		min_idx++;
    	}
    }
    
    public static void swap(int arr[], int a, int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}