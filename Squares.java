import java.util.Scanner;

public class Squares {
    int area;
    int topRight;
    int bottomLeft;
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user for input
        //System.out.print("Enter three integers separated by spaces: ");
        
        // Read the input line
        String input = scanner.nextLine();

        // Split the input string by spaces
        String[] inputStrings = input.split(" ");

        // Ensure there are exactly 3 integers
        if (inputStrings.length != 3) {
            System.out.println("Invalid input. Please enter exactly three integers.");
            return;
            
        }
        scanner.close(); // Close the scanner because we're done with input

        // Parse the integers
        try {
            int N = Integer.parseInt(inputStrings[0]);
            int K = Integer.parseInt(inputStrings[1]);
            int L = Integer.parseInt(inputStrings[2]);

            

            for (int i = 0; i <= N - 1; i++) { // Square iteration
                int bottomLeft = (i * K) - L;
                int topRight = (i * K) + L;
                System.out.println(bottomLeft + ", " + bottomLeft + "\n" 
                + bottomLeft + ", " + topRight + "\n"
                + topRight + ", " + topRight + "\n"
                + topRight + ", " + bottomLeft + "\n");

                int area = ((topRight - bottomLeft) * (topRight - bottomLeft));
                System.out.println(area);
                
                int[][] squares = new int[N][4]; // Each square has 4 coordinates: x1, y1, x2, y2
                squares[i][0] = bottomLeft;          // x1 (bottom left x)
                squares[i][1] = bottomLeft;     // y1 (bottom left y)
                squares[i][2] = topRight;    // x2 (top right x)
                squares[i][3] = topRight;       // y2 (top right y)
                System.out.println("Square " + i + ": (" + squares[i][0] + ", " + squares[i][1] + ") to (" + squares[i][2] + ", " + squares[i][3] + ")");

            }

            // Print the integers
            //System.out.println("You entered: " + N + " " + K + " " + L);

        } 
        catch (NumberFormatException e) {
            System.out.println("Invalid input. Please ensure you enter integers.");
        }

        


    }
}
