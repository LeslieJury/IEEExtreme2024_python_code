import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class LineIntersection {

    static int L = 0; // Length of the side of the square
    static List<Point> edgePoints = new ArrayList<>(); // Store the points on the edge of the square

    // Helper class to represent a point
    static class Point {
        double x, y;

        Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    public static List<Point> intersectionPoints(List<int[]> lines, int L) {
        List<Point> points = new ArrayList<>();
        for (int i = 0; i < lines.size(); i++) {
            for (int j = i + 1; j < lines.size(); j++) {
                int[] line1 = lines.get(i);
                int[] line2 = lines.get(j);
                
                double x1 = line1[0], y1 = line1[1], x2 = line1[2], y2 = line1[3];
                double x3 = line2[0], y3 = line2[1], x4 = line2[2], y4 = line2[3];
                
                double denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
                
                if (denom != 0) {
                    double t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom;
                    double s = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / denom;

                    if (0 <= t && t <= 1 && 0 <= s && s <= 1) {
                        double x = x1 + t * (x2 - x1);
                        double y = y1 + t * (y2 - y1);
                        
                        // Check if intersection point lies on the edge of the square
                        if (0 < x && x < L && 0 < y && y < L) {
                            points.add(new Point(x, y));
                        }
                    }
                }
            }
        }

        // Remove duplicate points
        List<Point> uniquePoints = new ArrayList<>();
        for (Point p : points) {
            boolean isDuplicate = false;
            for (Point up : uniquePoints) {
                if (Math.abs(p.x - up.x) < 1e-10 && Math.abs(p.y - up.y) < 1e-10) {
                    isDuplicate = true;
                    break;
                }
            }
            if (!isDuplicate) {
                uniquePoints.add(p);
            }
        }

        return uniquePoints;
    }

    public static int countAreas(List<int[]> lines, int L) {
        List<Point> points = intersectionPoints(lines, L);
        int V = points.size() + edgePoints.size() + 4; // intersection points + points on the sides of square + 4 corners
        
        int E = points.size() * 2 + lines.size() + edgePoints.size() + 4;
        // The segment lines number = inner intersection points + segment lines on the edge = (edge points + 4 corners)
        int F = 2 - V + E; // Euler's formula
        return F - 1; // remove the outer area
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] L_M_N = scanner.nextLine().split(" "); // Get the length of each side of the square, the number of lines from the origin, and the number of lines from (0, L)
        
        L = Integer.parseInt(L_M_N[0]); // Get the length of each line of the square
        int numALines = Integer.parseInt(L_M_N[1]);
        int numBLines = Integer.parseInt(L_M_N[2]);
        
        List<int[]> lines = new ArrayList<>(); // Store all lines x1, y1 & x2, y2

        for (int i = 0; i < numALines; i++) { // Get lines starting from the origin
            String[] j = scanner.nextLine().split(" ");
            if (j[0].equals("U")) {
                lines.add(new int[]{0, 0, Integer.parseInt(j[1]), L});
                edgePoints.add(new Point(Integer.parseInt(j[1]), L));
            } else if (j[0].equals("R")) {
                lines.add(new int[]{0, 0, L, Integer.parseInt(j[1])});
                edgePoints.add(new Point(L, Integer.parseInt(j[1])));
            }
        }

        for (int i = 0; i < numBLines; i++) { // Get lines starting from point (L, 0)
            String[] j = scanner.nextLine().split(" ");
            if (j[0].equals("U")) {
                lines.add(new int[]{L, 0, Integer.parseInt(j[1]), L});
                edgePoints.add(new Point(Integer.parseInt(j[1]), L));
            } else if (j[0].equals("L")) {
                lines.add(new int[]{L, 0, 0, Integer.parseInt(j[1])});
                edgePoints.add(new Point(0, Integer.parseInt(j[1])));
            }
        }

        int areas = countAreas(lines, L);
        System.out.println(areas);

        scanner.close();
    }
}
