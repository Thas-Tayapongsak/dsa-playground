#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
    // Validate command line arguments
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <your_name>" << std::endl;
        return 1; 
    }

    string your_name = argv[1];
    vector<string> msg_start {"Hello", "C++", "World", "to"};
    vector<string> msg_end {"from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg_start)
    {
        cout << word << " ";
    }
    cout << your_name << " ";
    for (const string& word : msg_end)
    {
        cout << word << " ";
    }   
    cout << endl;
}
