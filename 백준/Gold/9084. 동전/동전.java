import java.util.*;
import java.io.*;
public class Main{
	public static void main(String[] args)throws IOException{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb=new StringBuilder();
		int t=Integer.parseInt(br.readLine());
		for(int a=0;a<t;a++){
			int n=Integer.parseInt(br.readLine());
			int[] arr=new int[n];
			st=new StringTokenizer(br.readLine());
			for(int i=0;i<n;i++){
				arr[i]=Integer.parseInt(st.nextToken());
			}
			int m=Integer.parseInt(br.readLine());
			
			int[][]dp=new int[n][m+1];
			dp[0][0]=1;
			for(int i=0;i<=m;i+=arr[0]){
				dp[0][i]=1;
			}
			for(int i=1;i<n;i++){
				for(int j=0;j<=m;j++){
					if(arr[i]<=j){
						dp[i][j]+=dp[i][j-arr[i]];
					}
					dp[i][j]+=dp[i-1][j];
				}
			}
			sb.append(dp[n-1][m]).append("\n");
		}
		System.out.println(sb);
	}
}