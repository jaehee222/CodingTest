import java.util.Scanner;
import java.util.Arrays;

public class Greedy_2 {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int result = 10001;

        int arr[] = new int[M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[j] = sc.nextInt();
            }
            Arrays.sort(arr);
            // 각 열의 가장 작은 수
            if (i == 0 || result < arr[0]) {
                result = arr[0];
            }
        }

        System.out.println(result);
    }
}
