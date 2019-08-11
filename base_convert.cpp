#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
using namespace std;

int to_power(int base, int exponent)
{
	int value = 1;
	for(int i = 0; i < exponent; i++)
	{
		value *= base;
	}
	return value;
}

int convert_to_decimal(int num = 0, int base = 10) //Can't convert to hex
{
	string nums = to_string(num);
	int value = 0;

	vector<char> num_list;
	for(int i = 0; i < nums.length(); i++)
	{
		num_list.push_back(nums[i]);
	}

	int n = num_list.size();

	for(int i = 0; i < num_list.size(); i++)
	{
		value += (num_list[i] - '0') * to_power(base, n-1);
		n--;
	}

	return value;
}

string flip(string s)
{
	string flipped;
	int i;
	int j = s.length() - 1;
	for(i = 0; i < s.length(); i++)
	{
		flipped[i] = s[j];
		j--;
	}
	return flipped;
}

int convert_to_base(int number = 0, int base = 10, bool steps = false) //Hex not supported
{
	string value;
	int mod = 0;
	int my_div = 0;

	while((my_div != 1) or (my_div != 0))
	{
		mod = number % base;
		value += to_string(mod);
		if(steps)
		{
			cout<<number<<" mod "<<base<<" = "<<mod<<endl;
		}
		my_div = div(number, base).quot;
		if(steps)
		{
			cout<<number<<" div "<<base<<" = "<<my_div<<endl<<endl;
		}

		number = my_div;

		if(my_div == 0)
		{
			return stoi(flip(value));
		}

		else if(my_div == 1)
		{
			value += to_string(my_div);
			return stoi(flip(value));
		}
	}
	return stoi(flip(value));
}

int main()
{
	int a = 64;
	int bin = convert_to_base(a, 2, 1);
	cout<<bin<<endl;
	return 0;
}
