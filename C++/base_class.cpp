#include "base_convert.cpp"

class Converter
{
private:
	int original_num;
	int original_base;
public:
	Converter(int new_num, int new_base)
	:original_num(new_num), original_base(new_base)
	{}

	int to_decimal()
	{
		return convert_to_decimal(original_num, original_base);
	}

	int to_base(int other_base)
	{
		return convert_to_base(this->to_decimal(), other_base);
	}
};


int main()
{
	Converter c = Converter(1100100, 2);
	cout<<c.to_decimal()<<endl;

	cout<<c.to_base(7)<<endl;
	return 0;
}
