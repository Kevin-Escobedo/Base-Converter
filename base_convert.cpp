#include <iostream>
#include <string>
#include <vector>
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

int convert_to_decimal(int num = 0, int base = 10)
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

int main()
{
	int a = convert_to_decimal(101, 2);
	cout<<a<<endl;
}
