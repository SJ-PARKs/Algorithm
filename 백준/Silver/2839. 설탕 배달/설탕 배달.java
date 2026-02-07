import java.util.*;
import java.io.*;

public class Main{
	public static void main(String args[]) throws IOException{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int N=Integer.parseInt(st.nextToken());
		int n=N/3;
		boolean flag=false;
		for(int i=0;i<=n;i++){
			if((N-3*i)%5==0){
				System.out.println(i+(N-3*i)/5);
				flag=true;
				break;
			}
		}
		if(!flag){
			System.out.println(-1);
		}
		
	}
}