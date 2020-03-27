//Author: Kevin C. Escobedo
//Email: escobedo001@gmail.com
import java.util.*;

public class BaseConvert
{
	public BaseConvert()
	{

	}

	public int to_power(int base, int exponent)
	{
		int value = 1;
		for(int i = 0; i < exponent; ++i)
		{
			value *= base;
		}
		return value;
	}

	public int convert_to_decimal(int num, int base)
	{
		String nums = Integer.toString(num);
		Vector v = new Vector(10, 2);
		int value = 0;

		int nums_length = nums.length();

		for(int i = 0; i < nums_length; i++)
		{
			v.add(nums.charAt(i));
		}

		int n = v.size();

		for(int i = 0; i < v.size(); i++)
		{
			int temp = Integer.parseInt(String.valueOf(v.get(i)));
			value += temp * to_power(base, n-1);
			n--;
		}

		return value;
	}
}
