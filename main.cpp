
#include <bits/stdc++.h>
using namespace std;
#define ll long long

unordered_map<int, unordered_map<string,string>> timetable;
unordered_map<int, unordered_map<string,string>> teacher_schedule;
unordered_map<int, unordered_map<string,string>> rem;

vector<string> classes = {"Class 6A", "Class 6B", "Class 7A", "Class 7B"};
vector<string> sub = {"Mathematics", "Science", "English", "Social Studies", "Computer Science", "Physical Education"};
vector<string> days_of_week  = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
int periods_per_day =6 ;
unordered_map<string, unordered_map<string, int>> class_subject_periods = {
    {"Class 6A", {{"Mathematics", 6}, {"Science", 6}, {"English", 6}, {"Social Studies", 6}, {"Computer Science", 3}, {"Physical Education", 3}}},
    {"Class 6B", {{"Mathematics", 6}, {"Science", 6}, {"English", 6}, {"Social Studies", 6}, {"Computer Science", 3}, {"Physical Education", 3}}},
    {"Class 7A", {{"Mathematics", 6}, {"Science", 6}, {"English", 6}, {"Social Studies", 6}, {"Computer Science", 4}, {"Physical Education", 2}}},
    {"Class 7B", {{"Mathematics", 6}, {"Science", 6}, {"English", 6}, {"Social Studies", 6}, {"Computer Science", 4}, {"Physical Education", 2}}}
};

unordered_map<string, vector<string>> teachers = {
    {"Mr. Kumar", {"Mathematics"}},
    {"Mrs. Sharma", {"Mathematics"}},
    {"Ms. Gupta", {"Science"}},
    {"Mr. Singh", {"Science", "Social Studies"}},
    {"Mrs. Patel", {"English"}},
    {"Mr. Joshi", {"English", "Social Studies"}},
    {"Mr. Malhotra", {"Computer Science"}},
    {"Mr. Chauhan", {"Physical Education"}}
};



bool can_assign(string day, int period, string cls, string subject, string teacher, unordered_map<string, unordered_map<string, set<int>>> &teacher_schedule) {
    if (teacher_schedule[teacher][day].count(period) > 0) return false;
    return true;
}


void generate_timetable(){
    map<string, map<int,map<string, pair<string,string>>>>tt; 
    unordered_map<string, unordered_map<string,int>> rem = class_subject_periods;
    unordered_map<string, unordered_map<string,set<int>>>teacher_schedule;
    for (const string& day:days_of_week) {
        for (int i=1; i<=periods_per_day; ++i) {
            for (const string& cls :classes) {
                for (const auto& [subject,i] : class_subject_periods[cls]) {
                    for (const auto& [teacher, studs]:teachers) {
                        if (can_assign(day,i,cls,subject,teacher, teacher_schedule)) {
                            tt[day][i][cls] = {subject, teacher};
                            teacher_schedule[teacher][day].insert(i);
                            rem[cls][subject]--;
                            break;
                        }
                    }
                }
            }
        }
    }

    for (const string &day:days_of_week) {
        cout << day << ":\n";
        for (int period = 1;period<=periods_per_day; ++period) {
            cout << "  Period " << period << ":\n";
            for (const string &cls : classes) {
                if (tt[day][period].count(cls)) {
                    cout<< cls << tt[day][period][cls].first << " will be taken b " << tt[day][period][cls].second << "\n";
                }
            }
        }
    }
    

    
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    // Your code here
    
    generate_timetable();

       

   
    return 0;
}
