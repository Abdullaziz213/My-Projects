import board
import digitalio
import storage


switch = digitalio.DigitalInOut(board.D13)


switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP


storage.remount("/", switch.value)  # Hier "True" für schreibgeschützt
