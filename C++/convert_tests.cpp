#include "base_convert.cpp"
#include <gtest/gtest.h>

TEST(ConvertTest, toPower)
{
	int a = 2;
	ASSERT_EQ(4, to_power(a, 2));

	int b = 5;

	ASSERT_EQ(9765625, to_power(b, 10));
}

TEST(ConvertTest, toDecimal)
{
	int a = 101;
	int b = 10201;

	int con_a = convert_to_decimal(a, 2);
	int con_b = convert_to_decimal(b, 3);

	ASSERT_EQ(5, con_a);
	ASSERT_EQ(100, con_b);
}

TEST(ConvertTest, toBase)
{
	int a = 6;
	int b = 10;

	int con_a = convert_to_base(a, 2, 0);
	int con_b = convert_to_base(b, 5, 0);

	ASSERT_EQ(110, con_a);
	ASSERT_EQ(20, con_b);
}
	
int main(int argc, char** argv)
{
	testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
