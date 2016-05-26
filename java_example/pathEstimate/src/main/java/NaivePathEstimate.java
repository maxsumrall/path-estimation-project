import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class NaivePathEstimate
{
    public static void main( String[] args ) throws IOException
    {
        assert(args.length == 3);
        System.out.println(123);
        InputStreamReader inputStreamReader = new InputStreamReader( System.in );
        BufferedReader br = new BufferedReader( inputStreamReader);

        String s = br.readLine();
        while(!s.equals( "" ))
        {
            System.out.println(456);
            s = br.readLine();
        }
    }
}
