# Youtube to mp3 downloader

Use this tool to efficiently download any public content from youtube as a mp3 file

### Installation

```bash
git clone https://github.com/FluffySnowman/youtube-mp3-downloader.git

python3 -m pip install -r requirements.txt
```

#### Linux

Use your package manager to download tkinter for python. Heres an example for apt:-

```bash
sudo apt-get update

sudo apt-get install python3-tk
```

#### How to use / Executing

You will find two python files in the cloned directory. One is for gui and one is for cli downloading.

To run the gui version run this command in your terminal inside the directory:-

```bash
python3 Download.py
```

After this there will be an input box. Enter the link in the box and click on the 'Download' button.
After this, look at your terminal- the output of the download process will be shown in the terminal where you have run the Download.py file.

After the download is done, feel free to check out the current folder for the mp3 of the video that you just downloaded.


To run the cli version run this command in your terminal inside the directory:-

```bash
python3 Download-cli.py
```

You will be prompted to enter the link of the video you want to download. 
