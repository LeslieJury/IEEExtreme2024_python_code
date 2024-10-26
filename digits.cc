#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <string>

using namespace std;

// Helper class to represent a point
class Point {
public:
    double x, y;

    Point(double x, double y) : x(x), y(y) {}
};

// Function to find the intersection points of the lines
vector<Point> intersectionPoints(const vector<vector<int>>& lines, int L) {
    vector<Point> points;
    
    for (size_t i = 0; i < lines.size(); i++) {
        for (size_t j = i + 1; j < lines.size(); j++) {
            const auto& line1 = lines[i];
            const auto& line2 = lines[j];
            
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
                        points.emplace_back(x, y);
                    }
                }
            }
        }
    }

    // Remove duplicate points
    set<pair<double, double>> uniquePoints;
    vector<Point> result;

    for (const auto& p : points) {
        uniquePoints.insert({p.x, p.y});
    }

    for (const auto& p : uniquePoints) {
        result.emplace_back(p.first, p.second);
    }

    return result;
}

// Function to count areas formed by the lines
int countAreas(const vector<vector<int>>& lines, int L) {
    vector<Point> points = intersectionPoints(lines, L);
    int V = points.size() + 4; // intersection points + 4 corners of the square
    int E = points.size() * 2 + lines.size() + 4; // edges
    int F = 2 - V + E; // Euler's formula
    return F - 1; // remove the outer area
}

int main() {
    int L, numALines, numBLines;
    cin >> L >> numALines >> numBLines;
    vector<vector<int>> lines;

    for (int i = 0; i < numALines; i++) {
        string direction;
        int length;
        cin >> direction >> length;
        
        if (direction == "U") {
            lines.push_back({0, 0, length, L});
        } else if (direction == "R") {
            lines.push_back({0, 0, L, length});
        }
    }

    for (int i = 0; i < numBLines; i++) {
        string direction;
        int length;
        cin >> direction >> length;
        
        if (direction == "U") {
            lines.push_back({L, 0, length, L});
        } else if (direction == "L") {
            lines.push_back({L, 0, 0, length});
        }
    }

    int areas = countAreas(lines, L);
    cout << areas << endl;

    return 0;
}
