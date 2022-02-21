import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();

        String temp = "";
        String arr[] = new String[number];

        for(int x=0; x<number; x++){
            arr[x] = sc.next();
        }

        HashSet<String> hashSet = new HashSet<>(Arrays.asList(arr));
        String[] resultArr = hashSet.toArray(new String[0]);

        for(int i=0; i<resultArr.length; i++){
            for(int j=0; j<resultArr.length; j++){
                if(i==j) continue;
                else{
                    if(resultArr[i].length()<resultArr[j].length()){
                        temp = resultArr[i];
                        resultArr[i] = resultArr[j];
                        resultArr[j] = temp;
                    }
                }
            }
        }
        for(String el : resultArr){
            System.out.println(el);
        }
    }
}

