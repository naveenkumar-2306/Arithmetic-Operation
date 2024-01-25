#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

int guess;
int total;

class quiz {

protected:

	string ques;
	string ans1;
	string ans2;
	string ans3;
	string ans4;
	int correct_ans;
	int score;

public:
	//int total;
	void question( string , string ,string ,string ,string, int, int); 
	virtual void askq() = 0;
	
	int performance() {
		cout << "total score = " << total << " out of 100"<< endl;
		if (total >= 70 ){
			cout << "you have passed the quiz."<< endl;
			}
		else{
		 	cout << "better luck next time" << endl;
		 	}
		 return 0;
		 }
};

void quiz :: question( string q, string a1 , string a2, string a3, string a4, int ca, int s){
	ques = q;
	ans1 = a1;
	ans2 = a2;
	ans3 = a3;
	ans4 = a4;
	correct_ans = ca;
	score = s;
}

class mcq: public quiz{

public:
	virtual void askq() override{
		
		cout << ques << endl;
		cout << "1. "<< ans1 << endl;
		cout << "2. "<< ans2 << endl;
		cout << "3. "<< ans3 << endl;
		cout << "4. "<< ans4 << endl;
		cout << endl;
		
		cout << "give your ans in number:"<< endl ;
		cin >> guess;
		
		if (guess == correct_ans){
			cout << "correct! "<< endl;
			total += score;
			}
		else{
			cout<< "wrong!" <<endl;
			cout<< "correct ans is "<< correct_ans << endl;
			}
		}
};

class true_false : public quiz{

public:
	virtual void askq() override{
		
		cout << ques << endl;
		cout << "1. "<< ans1 << endl;
		cout << "2. "<< ans2 << endl;
		cout << endl;
		
		cout << "give your ans in number:"<< endl;
		cin >> guess;
		
		if (guess == correct_ans){
			cout << "correct! "<< endl;
			total += score;
			}
		else{
			cout<< "wrong!" <<endl;
			cout<< "correct ans is "<< correct_ans << endl;
			}
		}
};

class user {

private:
	string name;
	quiz* q;

public: 
	user (string name_val, quiz* quiz_val){
		name = name_val;
		q = quiz_val;
		}
	virtual void askq() {
		return;
		}
		
	string append_file () {
		std:: ostringstream oss;
		oss << total;
		string num = oss.str();
		
		return name + " have scored " + num ;
		}
	};


int main () {

	ofstream out_file { " output.txt" , std::ios::app};
	if (!out_file){
		std::cerr << "error creating the file " << endl;
		return 1;
		}
	string line;


	int number;
	cout << "how many are going to take quiz ?" << endl;
	cin >> number;
	
	for (int i =0 ; i< number; i++){
	
		quiz *q1 ;
	 	quiz *q2 ;
		
		int type;

		cout << " press enter to start the quiz : " << endl;
		cin.get();
		
		string name ;
		
		cout << "enter your name : " <<endl;
		cin >> name;
		
		cout << "enter what type of quiz you want (1. mcq , 2. true/ false) " << endl;
		cin >> type;
		
		if (type == 1){
			q1 = new mcq() ;
			q2 = new mcq() ;
			
			q1->question ( "1. Which one of the following river flows between Vindhyan and Satpura ranges? " , "Narmada" , "Mahanadi" , "Son" , "Netravati" , 1 , 50);
			
			q2->question ( "2. The Central Rice Research Station is situated in? " , "Chennai" , " Cuttack" , "Bangalore" , "Quilon" , 2 , 50);
			
			q1->askq();
			q2->askq();
			
			}
			
		else {
			q1 = new true_false() ;
			q2 = new true_false() ;
			
			q1->question ( "1.Sharks are mammals. " , "True" , "False" , "T" , "f" , 2 , 50) ;
			q2->question ( "2. Sea otters have a favorite rock they use to break open food. " , "True" , "False" , "T" , "f" , 1 , 50) ;
			
			q1->askq();
			q2->askq();
			
			}
			
		q2->performance();
		user p1 {name , q2};
		line =	p1.append_file ();
		out_file << line << endl;
		
		delete q1;
		delete q2;
		
		}
		
		
	return 0;
	}
	
