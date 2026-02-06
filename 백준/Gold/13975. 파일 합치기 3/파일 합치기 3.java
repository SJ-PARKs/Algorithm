import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < t; i++) {
            int k = Integer.parseInt(br.readLine());
            PriorityQueue<Long> pq = new PriorityQueue<>();
            st = new StringTokenizer(br.readLine());
            
            for (int j = 0; j < k; j++) {
                pq.add(Long.parseLong(st.nextToken()));
            }
            
            long hap = 0;
            while (pq.size() > 1) {
                long x = pq.poll();
                long y = pq.poll();
                long sum = x + y;
                hap += sum;
                pq.add(sum);
            }
            
            sb.append(hap).append("\n");
        }
        
        System.out.println(sb);
    }
}
