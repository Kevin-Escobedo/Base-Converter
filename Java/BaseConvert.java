//Author: Kevin C. Escobedo
//Email: escobedo001@gmail.com

public class BaseConvert
{
	public int to_power(int base, int exponent)
	{
		int value = 1;
		for(int i = 0; i < exponent; ++i)
		{
			value *= base;
		}
		return value;
	}
}
