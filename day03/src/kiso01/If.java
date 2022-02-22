package kiso01;

public class If {
    public void kiso01(){
        int v = 100;
        if(v%2==0){
            System.out.println("짝수");
        } else {
            System.out.println("홀수");
        }
    }

    public void kiso02(){
        float magnitude = 9.0F;
        if(magnitude >=8.0){
            System.out.println("진도 8이상");
        } else if(magnitude >=7.0){
            System.out.println("진도 7이상");
        } else if(magnitude >=6.0){
            System.out.println("진도 6이상");
        } else {
            System.out.println("진도6 ~ 8이상 이외");
        }
    }
}
