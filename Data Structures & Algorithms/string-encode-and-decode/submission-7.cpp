class Solution {
public:

    string encode(vector<string>& strs) {
        string str = "";
        for (const string& x : strs){
            str += to_string(x.length()) + "#" + x;
        }
        cout << str << endl;
        return str;
    };

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while (i < s.length()){
            int j = i;
            while (s[j] != '#'){
                j++;
            }
            int length = stoi(s.substr(i,j-i));
            i = j + 1;
            j = i + length;
            result.push_back(s.substr(i, j-i));
            i = j;
        }   
        return result;
    };
};
