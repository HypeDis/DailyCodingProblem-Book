"""
Implement a file syncing algorithm for two computers over a low-bandwidth network. 
What if we know the files in the two computers are mostly the same? 
"""

# first computer sends a list of file names(key) and md5 hashes(value)
# second computer sends a list of files that are not in sync
# first computer sends only those files back