#include <iostream>
#include <math.h>
#include <vector>
using namespace std;



// Sums the Divisors of a number
int getSumOfDivs(int num)
{
	int i = 2;
	double sqt = sqrt (num);
	int sum = 1;
	while ( i < sqt )
	{
		if (num % i == 0)
		{
			sum += i + num/i;
			//cout << i << endl;
		}
		i++;
	}
	return sum;

}

// Checks whether a number is Abundant
bool isAbundantNum(int num)
{
	if (getSumOfDivs(num) > num)
	{
		return true;
	}
	return false;
}

// Adds all abundant numbers less than a limit to an array
std::vector<int> calculateAllAbundants(int limit)
{
	int i;
	int index = 1;
	std::vector<int> abundants;
	for (i = 1; i < limit; i++)
	{
		if (isAbundantNum(i))
		{
			abundants.at(index) = i;
			index++;
			cout << i << endl;
		}
	}

	return abundants;
}

bool isSumOfAbundants(int num)
{

}

int main()
{
	vector<int> abundants = calculateAllAbundants(30);
	cout << abundants.at(1) << endl;
}