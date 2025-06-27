import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int m;
    static int[][] map;
    static int[][] chk;
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        chk = new int[n][m];
        DFS(0, 0);
        System.out.println(ans);
    }

    public static void DFS(int idx, int hap) {
        if (idx == n * m) {
            ans = Math.max(hap, ans);
            return;
        }
        int x = idx / m;
        int y = idx % m;
        if (chk[x][y] == 0) {
            if (x + 1 < n && y - 1 >= 0 && chk[x + 1][y] == 0 && chk[x][y - 1] == 0) {
                chk[x][y] = 1;
                chk[x + 1][y] = 1;
                chk[x][y - 1] = 1;
                DFS(idx + 1, hap + 2 * map[x][y] + map[x + 1][y] + map[x][y - 1]);
                chk[x][y] = 0;
                chk[x + 1][y] = 0;
                chk[x][y - 1] = 0;
            }
            if (x - 1 >= 0 && y - 1 >= 0 && chk[x - 1][y] == 0 && chk[x][y - 1] == 0) {
                chk[x][y] = 1;
                chk[x - 1][y] = 1;
                chk[x][y - 1] = 1;
                DFS(idx + 1, hap + 2 * map[x][y] + map[x - 1][y] + map[x][y - 1]);
                chk[x][y] = 0;
                chk[x - 1][y] = 0;
                chk[x][y - 1] = 0;
            }
            if (x - 1 >= 0 && y + 1 < m && chk[x - 1][y] == 0 && chk[x][y + 1] == 0) {
                chk[x][y] = 1;
                chk[x - 1][y] = 1;
                chk[x][y + 1] = 1;
                DFS(idx + 1, hap + 2 * map[x][y] + map[x - 1][y] + map[x][y + 1]);
                chk[x][y] = 0;
                chk[x - 1][y] = 0;
                chk[x][y + 1] = 0;
            }
            if (x + 1 < n && y + 1 < m && chk[x + 1][y] == 0 && chk[x][y + 1] == 0) {
                chk[x][y] = 1;
                chk[x + 1][y] = 1;
                chk[x][y + 1] = 1;
                DFS(idx + 1, hap + 2 * map[x][y] + map[x + 1][y] + map[x][y + 1]);
                chk[x][y] = 0;
                chk[x + 1][y] = 0;
                chk[x][y + 1] = 0;
            }
        }
        DFS(idx + 1, hap); 
    }
}
