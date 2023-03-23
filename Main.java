import java.security.Principal;
import java.util.Scanner;

/**
 * Main
 */
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
       int testcases = sc.nextInt();
       while (testcases != 0) {
        int lenofstring = sc.nextInt();    
        String string = sc.nextLine();
        System.out.println(check(lenofstring,sc.nextLine()));;    
        testcases--;
       }
    }

    private static String check(int lenofstring, String nextLine) {
        if(lenofstring < 2) return "No";
        else {
            for (int i = 2; i < lenofstring; i = i+2) {
                if(nextLine.charAt(i) != nextLine.charAt(i-1)){
                    return "No";
                }
            
            }
        }
        return "yes";
    }
}