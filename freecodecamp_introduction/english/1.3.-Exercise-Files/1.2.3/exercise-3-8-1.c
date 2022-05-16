/*
    PROGRAM:  exercise-3-8-1.c
    AUTHOR:   Haidar Al-Aubiydy
    DATE:
*/

/**************************************************************************
/* Declare include files
 **************************************************************************/
#include <stdio.h>
#include <stdlib.h>

/**************************************************************************
/* Defines
 **************************************************************************/
#define SIZE 100

/**************************************************************************
/* Function prototypes
**************************************************************************/
int toggle( int a[ ] );
int state( int a[ ] );


/**************************************************************************
 * Main
 **************************************************************************/
int main( void )
{
	int ar[SIZE] = {0};

	toggle(ar);
	state(ar);

	return EXIT_SUCCESS;
}

/**************************************************************************
 * Function: int toggle( char a[ ] )
 **************************************************************************/
int toggle( int a[ ] )
{
	int i=0;

	for(i=0; i<SIZE ; i++)
	{
	    if(a[i] == 0)
		{
		    a[i] = 1;
        }
		else if(a[i] == 1)

		{
			a[i] = 0;
		}
    }
	return 0;
}


/**************************************************************************
 * Function:  int state( char a[ ] )
 **************************************************************************/
int state( int a[ ] )
{
	int i=0;
	for(i=0 ; i<SIZE ; i++)
	{
	    printf("%d ", a[i]);
	}
	return 0;
}