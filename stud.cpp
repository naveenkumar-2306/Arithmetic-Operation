#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

void writefile(string n, int grad=-1)
{
    fstream ofile;
    ofile.open("output.txt",ios::app);
    if(grad==-1)
    {
        ofile<<"Student name is :"<<n<<endl;
        ofile<<"Courses:"<<endl;
    }
    else
    {   
        ofile<<"course: "<<n<<", grade: "<<grad<<endl;
    }
   
    ofile.close();
    
}

void writefile(float cgpa)
{
    fstream ofile;
    ofile.open("output.txt",ios::app);
    ofile<<"CGPA is: "<<cgpa<<endl;    
    ofile<<"___________________________________________"<<endl<<endl;
    ofile.close();
}
class Person {
protected:
    std::string name;

public:
    
    Person(std::string& n)
    {
        name = n;
    }

    // virtual void display(){
    //     std::cout << "Name: " << name << std::endl;}
      virtual void display() =0;  
    
};

class Course {
private:
    std::string courseName;
    int courseGrade;

public:
    Course(std::string& name, int grade)
    {
        courseName = name;
        courseGrade = grade;
    }
    int getGrade() {
        return courseGrade;
    }

    void display() {
        std::cout << "Course: " << courseName << ", Grade: " << courseGrade << std::endl;
    }
};

class Student : public Person {
private:
    std::vector<Course> courses;

public:
    Student(std::string& n) : Person(n) {}
    void addCourse(std::string& courseName, int grade) {
        courses.em pers = &stud;
                pers->display();place_back(courseName, grade);
    }

    void display(){
        cout<<"Name: "<<name<<endl  ;
        std::cout << "Courses:" << std::endl;
        for (auto& course : courses) {
            course.display();
        }
    }
    
    void addnewstud(std::string studentName)
    {
        std::string courseName;
        int grade;
        char addMore;
        writefile(studentName);
       
        do {
            std::cout << "Enter course name: ";
            std::cin >> courseName;
            std::cout << "Enter grade: ";
            std::cin >> grade;
            addCourse(courseName, grade);
            writefile(courseName,grade);
            std::cout << "Do you want to add another course? (y/n): ";
            std::cin >> addMore;
        } while (addMore == 'y' || addMore == 'Y');
    }

    float calculateAverageGrade() 
    {
        float totalGrade = 0.0;
        for (auto& course : courses) {
            totalGrade += course.getGrade();
        }
        return totalGrade / courses.size();
    }
};

int main() {
    std::vector<Student> students;
    int numStudents;
    int choice=1;
    std::string studentName;
    Student stud(studentName); 
    Person* pers;
    
    std::cout << "Enter the number of students: ";
    std::cin >> numStudents;
    
    for (int i = 0; i < numStudents; ++i) 
    {
        std::cout << "Enter student "<<i+1<<" name: ";
        std::cin >> studentName;
        Student stud(studentName); 
        stud.addnewstud(studentName);
        students.push_back(stud);
        float grad = stud.calculateAverageGrade(); 
        writefile(grad);
    }
    
    do{
        std::cout<<"Please enter your coice:\n1.display\t2.add new user\t3.exit\n";
        std::cin>>choice;
       if(choice==1)
       {
            for (auto& stud : students) 
            {
                std::cout<<std::endl;
                pers = &stud;
                pers->display();
                std::cout << "Average Grade: " << stud.calculateAverageGrade() << std::endl;
                std::cout << "------------------------" << std::endl;
            }
            continue;
       }
        else if(choice==2) 
        {   std::cout << "Enter student name: ";
            std::cin >> studentName;
            Student stud(studentName); 
            stud.addnewstud(studentName);
            students.push_back(stud);
            float grad = stud.calculateAverageGrade(); 
            writefile(grad);
            continue;
        }    
        else if(choice ==3)
        {
            exit(0);
        }        
        else 
            std::cout<<"Sorry wrong, please enter choice again";
        
    }while(choice!=0);
   return 0;
}
