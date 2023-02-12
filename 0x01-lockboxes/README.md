# 0x01. Lockboxes
`n` number of locked boxes is placed infront of a person. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.
`0-lockboxes.py` contains a method that determines if all the can be opened.
* Prototype: `def canUnlockAll(boxes)`
* `boxes` is a list of lists
* A key with the same number as a box opens that box
* It is assumed that all keys will be positive integers
	- There can be keys that do not have boxes
* The first `box[0]` is unlocked
* Returns `True` if all boxes can be opened, else `False` is returned
```
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
```
```
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```
