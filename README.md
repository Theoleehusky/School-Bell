# School Bell
A botched discord bot (meant for my school).

(For myself to look back in a few years and cringe at)

![alt text](https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/socialmedia/emoji-one/104/bell_1f514.png)

*Image under free liscence from joypixels.

## Setup
Create token.txt under references and paste bot token.
To turn on the school bell functionality, uncomment line 11 and replace server ids (line 50, 51).

## Functionalities
* Custom text responses
* Automated school bell
(Joins all populated voice channels at set times to play the bell)
   
* Image responses (currently sends online school schedule)
* Looks up type of school day
* Customized bot activity (watching you)
* Count of coronavirus cases from webscraping ([Worldmeters](worldometers.info/coronavirus))
* Calls khan for some calculus help

## imports
* discord for obvious reasons
* re (regular expressions) for message parsing
* bs4 for coronavirus case webscraping

## Todo
* "stop" command to kick bot