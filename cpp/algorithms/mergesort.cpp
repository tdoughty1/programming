#include <iostream>
#include <iomanip>
#include <vector>
#include <time.h>

using namespace std;

void qmerge(vector<float>& vector_out, vector<float>& veca, vector<float>& vecb)
{
    int imax = veca.size();
    int jmax = vecb.size();
    int kmax = vector_out.size();

    int i = 0;
    int j = 0;
    int k = 0;

    while(k < kmax)
    {
        // Check if at end of either array
        if(i == imax)
        {
            while(j < jmax)
            {
                vector_out.at(k) = vecb.at(j);
                j++;
                k++;
            }
            break;
        }

        if(j == jmax)
        {
            while(i < imax)
            {
                vector_out.at(k) = veca.at(i);
                i++;
                k++;
            }
            break;
        }

        // Standard Case
        if(veca.at(i) < vecb.at(j))
        {
            vector_out.at(k) = veca.at(i);
            i++;
            k++;
        }
        else
        {
            vector_out.at(k) = vecb.at(j);
            j++;
            k++;
        }
    }
}

void mergesort(vector<float>& vector_in)
{
    int n = vector_in.size();
    if(n != 1)
    {
        vector<float> veca(&vector_in[0], &vector_in[n/2 + n%2]);
        vector<float> vecb(&vector_in[n/2 + n%2], &vector_in[n]);

        mergesort(veca);
        mergesort(vecb);

        qmerge(vector_in, veca, vecb);
    }
}

int main()
{
    int n = 1000000;

    for(int j = 0; j < 10; j++)
    {
        // Initialize Arrays
        vector<float> vector_in(n);

        srand((unsigned)time(0));
        for(int i=0; i<n; i++)
        {
            vector_in.at(i) = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
        }

        clock_t start = clock();
        for(int i=0; i<10; i++)
        {
            mergesort(vector_in);
        }
        clock_t finish = clock();
        cout << "Algorithm took " << fixed << setprecision(2) << (float(finish-start)/CLOCKS_PER_SEC)*100 << " ms for n = " << n << endl;
    }
}
