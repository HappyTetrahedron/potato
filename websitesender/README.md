# Website Sender

This is a small program used to send a URL from one device to another via UDP. The receiving device will open the URL in a browser and also keep a history of most recent URLs.

I use this to display recipes on potato as it hangs in my kitchen.

Note that this is a very rudamentary C program that I hacked together one late evening. It works well enough for me but it might contain bugs or exploits.

### websitesender
The websitesender takes three arguments: A hostname to send to, a port, and an url to send to the receiver. It will then send out an UDP packet and exit. Note that UDP packets are not guaranteed to arrive at their target and my program implements no check whatsoever on whether the packet has arrived. It's never been a problem on my local network though.

### websiteserver
The websiteserver takes one argument: a port on which to listen for incoming packets. It is supposed to be running in the background. When it receives a packet, it interprets its contents as a string and tries to open it in firefox-nightly. The packet contents aren't checked in any way.

It also stores the received string in a file to keep a history of the most recent received URLs. That file is in dzen2 config format.

### websitemenu
The websitemenu folder contains three scripts that work together and can be used to display the list of recently received URLs. The list is displayed on screen using dzen2. The entries are clickable. Clicking on an entry will result in that website being opened again.

To display the menu, run showwebsites. You need to have dzen2 installed. openwebsite is used by dzen2 to open a website after clicking on it. quit is used by dzen2 to quit the menu without opening a website.

## portability
The code contains hard-coded absolute file paths that you will need to adjust in order to use it. You will need to modify websiteserver.c and showwebsites.

I know full well that this code is horrible. Feel free to fork and improve.
