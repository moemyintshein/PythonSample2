# with open('test.txt', 'r') as rf:
# 	with open('test_copy.txt', 'w') as wf:	#copy test.txt as test_copy.txt

# 		for line in rf:
# 			wf.write(line)

# with open('github.jpeg', 'rb') as rf:
# 	with open('github_copy.jpeg', 'wb') as wf:


# 		for line in rf:
# 			wf.write(line)

with open('gitlab.png', 'rb') as rf:
	with open('gitlab_copy.png', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)

		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)