#include <stdio.h>

int main()
{
    int t;
    scanf("%d", &t);
    double l, ta, ca,w,r;

    for (int i = 0; i < t; i++)
    {
        scanf("%lf", &l);
        w = (l*6)/10;
        r = l/5.0;
        ta = l*w;
        ca = 3.141592*r*r;
        printf("%.2lf %.2lf\n", ca, ta - ca);
    }
    return 0;
}
