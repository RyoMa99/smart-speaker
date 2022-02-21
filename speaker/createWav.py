import subprocess
import os

TEXT_FILE = "sample.txt"

# openjtalk
X_DIC = "/var/lib/mecab/dic/open-jtalk/naist-jdic"
M_VOICE = "/usr/share/hts-voice/mei/mei_normal.htsvoice"
R_SPEED = "1.0"
OW_WAVFILE = "./sample.wav"

def talk_text(text):
    open_jtalk = ["open_jtalk"]
    xdic = ["-x", X_DIC]
    mvoice = ["-m", M_VOICE]
    rspeed = ["-r", R_SPEED]
    owoutwav = ["-ow",OW_WAVFILE]
    cmd = open_jtalk + xdic + mvoice + rspeed + owoutwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    c.stdin.write(text.encode("utf-8"))
    c.stdin.close()
    c.wait()
    wr = subprocess.Popen(["paplay", OW_WAVFILE])
    wr.wait()

def main():
  with open(f"{os.path.dirname(__file__)}/../{TEXT_FILE}") as f:
    for line in f:
      talk_text(line)

if __name__ == "__main__":
  main()