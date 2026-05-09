""" Answer "Yes" only for these inputs:
42
forty-two
forty two
    Otherwise the answer is "No"
"""

answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip() # here in input must be spaces cut out!

if answer == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two":  #if input contains big cases or lower cases
    print("Yes")
else:
    print("No")
