#include<stdio.h>
int main()
{   int a;
    printf("Enter number of elements : ");
    scanf("%d", &a);
    
	int at[a]={};
	int bt[a]={};
	int ct[a]={};
	int wt[a]={};
	int tat[a]={};
	for(int i=0;i<a;i++)
	{
		printf("\nenter AT for p%d: ",i);
		scanf("%d",&at[i]);
		printf("enter BT for p%d: ",i);
		scanf("%d",&bt[i]);
	}
	ct[0]=0;
	for(int k=0;k<a;k++)
	{
		ct[k]=ct[k-1]+bt[k];
	}
	for(int m=0;m<a;m++)
	{
		wt[m]=ct[m]-(at[m]+bt[m]);
	}
	for(int n=0;n<a;n++)
	{
		tat[n]=wt[n]+bt[n];
	}
	printf("\nP ID\tAT\tBT\tCT\tWT\tTAT");
	for(int j=0;j<a;j++)
	{
		printf("\np%d\t%d\t%d\t%d\t%d\t%d",j,at[j],bt[j],ct[j],wt[j],tat[j]);
	}
	
	return 0;
}