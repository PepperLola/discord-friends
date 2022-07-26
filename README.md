# Discord Friend Finder

TLDR:
This script will compile a list of every user you've sent messages to on Discord in the event that you want to re-add someone but don't remember their username. For example, if you get hacked and they block all of your friends, you can use this as a way to figure out who you were friends with and who you would want to add back. You have to request your data from Discord, place the `friends.py` script in the messages directory of the data folder (called `package`), and run it. All it does is parse the `index.json` folder and output a list of the users you've sent **direct messages** to into a file called `friends.txt` in the same folder.

## Prerequisites

### Request your data from Discord

This is a very straightforward process, but it can take up to 30 days or so for Discord to process your request and send you the download link.

First, you must request your data from Discord. This can be achieved by going into settings in Discord, navigating to the <kbd>Privacy & Safety</kbd> tab, scrolling down to the bottom, and clicking <kbd>Request Data</kbd>.

![Request Data](https://raw.githubusercontent.com/PepperLola/discord-friends/main/img/request_data.png)

Now, you have to wait for Discord to process the request and send the download link to the email associated with your Discord account.

Once you've received the email with your data from Discord, you must download it. It will be a .zip archive called package.zip. Unzip it (into your downloads folder is fine).

### Download the script

Download the `friends.py` script from this repository and move it to the `messages` directory in your user data. You should also see a file called `index.json` in the same folder as the script.

### Run the script

Before running the script, you need to have Python installed. You can do so by downloading the installer from [here](https://www.python.org/downloads/). After you've done that, open the command prompt. You may be able to right click on the folder (or the background of your file manager when in the folder) and open a command prompt or terminal window there. If not, you must do it manually.

On Windows, you can search `cmd` and open the command prompt. On Mac, you can open Terminal from the spotlight. You must then navigate to the folder by using the `cd` command. If you need help with that, [this](https://linuxhint.com/cd-command-in-terminal/) is how you can use that command on Linux/MacOS, and [this](https://www.geeksforgeeks.org/cd-cmd-command/) is for Windows.

Once you've navigated to the folder, simply run the script by entering `python friends.py`. It will parse the `index.json` file and output a list of all your friends to `friends.txt` in the same folder. You can then open this file and see a list of friends for you to (potentially) add back. Note that it will also include bots and people you were never friends with, because it only lists people you DMed.

If you run the command with `-v` (`python friends.py -v`), it will prompt you to confirm whether or not you want to store each user in the list. If you type `y` and press enter, it will add them to the file, and if you type anything else (as long as it doesn't have a `y` in it, regardless of capitalization), it won't add them to the file.

## Example

I wrote this script to help my friend who had their Discord account hacked. [This](https://www.youtube.com/watch?v=0HtnCH1t4a8) was the scam that they fell for. If you don't want to watch the video, essentially the perpetrators set up a fake verification bot that had you scan a QR code using the Discord app (like you do to sign in using the QR codes). Your phone then gives them your Discord token because it thinks that they are Discord and that you're trying to sign in, and they now have full access to your account, regardless of if you had 2FA enabled. They then often do several things with your account, as detailed in the video, but the one thing they do that this script is designed to fix is remove all your friends.

Because there isn't a way to find a list of friends you've removed, a way that I found to see who you might want to add back is to download your Discord user data and look at who you've sent DMs to. Instead of having to look through the json file manually, I wrote this script to make the process easier. It's nothing much, and I would definitely recommend reaching out to Discord support before trying this (although I'm not implying that this method is dangerous at all, because it isn't).
