# 0x03. Log Parsing #
This directory contains a script that reads `stdin` line by line and computes the following metrics:
* Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (line is skipped if the format is not this one)
* After every 10 lines and/or a keyboard interruption (`CTRL + C`), the following statistics are printed from the beginning:
	- Total file size: `File size: <total size>`
	- where `<total size>` is the sum of all previous `<file size>` (input format above)
	- Number of lines by status code:
		* possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
