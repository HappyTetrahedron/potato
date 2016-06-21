/* A simple server in the internet domain using TCP
   The port number is passed as an argument */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <err.h>

void error(const char *msg)
{
    perror(msg);
    exit(1);
}

// Write the URL to a file in the format of a dzen config file. This is to keep a history of recent websites.
void write_website(char* website_str)
{
     // You will need to adjust the file path here
     FILE* infile = fopen("/home/user/websitemenu/websitelist", "r");
     if (infile == NULL)
          error("Could not open file");

     // You will need to adjust the file path here
     FILE* outfile = fopen("/home/user/websitemenu/new_websitelist", "w");
     if (outfile == NULL)
          error("Could not open file");

     char* line = NULL;
     size_t len = 0;
     ssize_t read;

     int linecounter = 0;

     // With my potato in portrait mode, I can fit 16 lines with my line height (configured in dzen2). 14 old entries + title + 1 new entry.
     while((read = getline(&line, &len, infile)) != -1 && linecounter < 14) 
     {
          if (linecounter == 1)
          {
               // You will need to adjust the file path here
               fprintf(outfile, "^ca(1, /home/user/websitemenu/openwebsite %s) %s ^ca()\n", website_str, website_str);
          }
          linecounter++;
          fprintf(outfile, "%s", line);
     }
     // You will need to adjust the file path here
     fprintf(outfile, "^ca(1, /home/user/websitemenu/quit ) Quit ^ca()\n");

     fclose(infile);
     fclose(outfile);

     // You will need to adjust the file paths here
     rename("/home/user/websitemenu/new_websitelist", "/home/user/websitemenu/websitelist");
}

// Handle a received packet
void handle_datagram(char* buffer, size_t count)
{
     printf("%s\n", buffer);
     
     int pid = fork();
     if(pid <= 0)
     {
          // I use firefox-nightly to display websites on potato. 
          execl("/usr/bin/firefox-nightly", "firefox-nightly", buffer, NULL);
     }
     
     // write the website to a history file
     write_website(buffer);
}

int main(int argc, char *argv[])
{
     int sockfd, newsockfd, portno;
     socklen_t clilen;
     char buffer[1024];
     struct sockaddr_in serv_addr, cli_addr;
     int n;
     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     sockfd = socket(AF_INET, SOCK_DGRAM, 0);
     if (sockfd < 0) 
        error("ERROR opening socket");
     bzero((char *) &serv_addr, sizeof(serv_addr));
     portno = atoi(argv[1]);
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);
     if (bind(sockfd, (struct sockaddr *) &serv_addr,
              sizeof(serv_addr)) < 0) 
              error("ERROR on binding");
     listen(sockfd,5);

     struct sockaddr_storage src_addr;
     while(1)
     {
          bzero(buffer,1024);
          clilen = sizeof(cli_addr);
          ssize_t count=recvfrom(sockfd,buffer,sizeof(buffer),0,
                   (struct sockaddr*)&src_addr,&clilen);
    
          if (count==-1)
               error("ERROR on receiving");
          else if (count==sizeof(buffer))
               warn("Buffer too small, message cut");
          else
               handle_datagram(buffer,count);
     }
     close(sockfd);
     return 0; 
}


