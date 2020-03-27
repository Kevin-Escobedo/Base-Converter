//Author: Kevin C. Escobedo
//Email: escobedo001@gmail.com

public class TestConvert
{
	public static void main(String[] args)
	{
		BaseConvert b = new BaseConvert();
		int num = 101;
		int dec = b.convert_to_decimal(num, 2);
		System.out.println(dec);
	}

}
