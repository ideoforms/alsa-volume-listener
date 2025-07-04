# Alsa volume listener

Listens for OSC `/set_volume` messages, and sets the Alsa system output volume accordingly.

## Usage

Create a virtual env, and run:

```
pip3 install -r requirements.txt
python3 run-volume-listener.py
```

Then, send an OSC message to port 13007 containing `set_volume <N>`, where `<N>` is a float between 0 and 1.
