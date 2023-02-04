import java.util.Scanner;

public class Greedy_2 {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        int result = 0;
        while (N != 1) {
            result++;
            if (N % K == 0) {
                N = N / K;
            } else {
                N -= 1;
            }
        }

        System.out.println(result);
    }
}
