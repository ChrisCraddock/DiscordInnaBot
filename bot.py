'''After installing Python and marking Include PATH
open your terminal or cmd line interface as administrator
and type: pip install discord.py
'''

import discord
from discord.ext import commands
import asynchat


bot = commands.Bot("*") #prefix including *

@bot.event
async def on_ready():
    print("Someone say food time?")

@bot.command(pass_context=True)
async  def Ping(ctx):
    await bot.say("```css\n"
                  "Meow Meow Mother Fluffer``` :joy_cat:") #will say whatever you put in there


@bot.command(pass_context=True)
async def Hello(ctx):
    await bot.say("```css\n"
                  "Hi Hi Hi!!!```")

@bot.command(pass_context=True)
async def Commands(ctx):
    await bot.say("```I'm a little kittay, Still learning new things.\n"
                  "Ping\n"
                  "Hello\n"
                  "Invite - Invite link to server\n"
                  "Summon\n"
                  "WinCmd - Basic Windows CLI !!NERD ALERT!!```")

@bot.command(pass_context=True)
async def Invite(ctx):
    await bot.say("https://discord.gg/9TmrFVk")

@bot.command(pass_context=True)
async def Summon(ctx):
    await bot.say("AYE Senpai!!:heart_eyes_cat:")

@bot.command(pass_context=True)
async  def WinCmd(ctx):
    await bot.say("```Command Line Interface: Basic Commands\n"
                  "Format: [command] [target (if any)] [switches]\n"
                  "-OR- [command] [switches (if and)] [target]\n"
                  "example: [dir] [/p (switch)] or [cd] [Cats (target)]\n"
                  "------------------------------------------------------------------------\n"
                  "/? is a switch that will list any avail switches for command\n"
                  "help   - for when you are really lost\n"
                  "exit   - exit/close the prompt\n"
                  "dir    - lists all contents in current directory\n"
                  "dir /p - shows directory 1 page at a time\n"
                  "dir /w - shows only filenames\n"
                  "cd \cats - change directory from current to target\n"
                  "cd cats - Also changes directory from current to target\n"
                  "cd\    - takes you back to root directory\n"
                  "cd ..  - moves you back one step in the file structure\n"
                  "[To go from C:\> drive to a different drive, just type the drive letter\n"
                  "example: C:\>D: (include colon)]\n"
                  "md [target] - make directory ie. md fuzzy creates a folder called fuzzy\n"
                  "mkdir [target] - make directory ie:mkdir fuzzy creates folder 'fuzzy'```")

    await bot.say("```------------------------Check Twice Delete Once-------------------------\n"
                  "rmdir [target] - removes the specified directory\n"
                  "Note: using command will not delete target if target not empty\n"
                  "rd [target] /s - removes the target and subfolders (/s is the switch)\n"
                  "del [target file] - removes target OR files inside folder"
                  "-------------------------Wildcard---------------------------------------\n"
                  "*      - a wildcard to find any files within that directory\n"
                  "[example: E:\>dir *.txt will find any files with .txt extension]\n"
                  "[example: E:\>dir f*.* will find any files starting with 'f']\n"
                  "-------------------------Move/Copy--------------------------------------\n"
                  "copy [target] [destination] - COPIES target to new path\n"
                  "[example: C:\>copy fuzzy e:\]\n"
                  "move [target] [destination] - MOVES target to new path\n"
                  "[example: C:\>move fuzzy e:\]\n"
                  "xcopy [target] [destination] [switch] - best to start off with xcopy /?\n"
                  "robocopy /? - just google it or try it in the prompt\n"
                  "-------------------------Utilities--------------------------------------\n"
                  "chkdsk /? - scans, detects, and repairs file system issues and errors\n"
                  "format /? - format volumes from the command line\n"
                  "hostname - Well would ya look at that, just look at it\n"
                  "sfc /? - System File Checker: scans, detects, restores important system\n"
                  " files, folders, and paths\n"
                  "shutdown /? - really? No, just go away if I need to explain\n"
                  "-------------------------Security---------------------------------------\n"
                  "gpupdate /?- update group policies from command line\n"
                  "gpresult /?- quick overview of policy results for a user\n"
                  "[example: C:\>gpresult /USER fuzzy /R]```")

#TODO: Add error handling














####################################################







####################################################








####################################################







####################################################








####################################################







####################################################

bot.run("NDk5NDQyMzAzNDg0NTU5MzYw.Dp8V-Q.Xdgm1fGc9QW-7i_fUz4DFDfoDqk")
