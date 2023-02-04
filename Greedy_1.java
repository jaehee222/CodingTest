import java.util.Scanner;

public class Greedy_1 {
    public static void main(String[] args) throws Exception {
        // 가장 큰 수 구하기 x
        // 두번째 큰 수 구하기 y
        // k 만큼 x를 더하고 y 한번 더하고 (반복.. 총M번이어야함)

        Scanner sc = new Scanner(System.in);
        // N개의 자연수 M번 더하기 K번 중복 가능
        int N = sc.nextInt();
        int M = sc.nextInt();
        int K = sc.nextInt();

        // 엔터값 지우기
        sc.nextLine();

        // 임의의 N개의 자연수
        String[] arrN = sc.nextLine().split(" ");

        int max = 0;
        int max2 = 0;
        int tmp;
        for (int i = 0; i < N; i++) {
            tmp = Integer.parseInt(arrN[i]);
            if (i == 0) {
                max = tmp;
            } else {
                if (max < tmp) {
                    // 이미 가장 큰 값이니..max2값 물려주고 continue..
                    max2 = max;
                    max = tmp;
                    continue;
                }
                if (max2 < tmp) {
                    max2 = tmp;
                }
            }
        }

        // 반복 카운트..
        int cnt = 0;
        int total = 0;
        for (int i = 0; i < M; i++) {
            // K번 연속 가능
            if (cnt == K) {
                total += max2;
                // 연속인 값 카운트
                cnt = 0;
            } else {
                total += max;
                cnt += 1;
            }
        }

        System.out.println(total);
    }
}
