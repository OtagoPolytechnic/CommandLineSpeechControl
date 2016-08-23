commandDict = {'Change Directory': 'cd', 'Display file’s contents': 'cat', 'Clear Command': 'clear', 'Copy Files': 'cp', 'Stop A Process': 'kill', 'List Directory': 'ls', 'Create New Directory': 'mkdir', 'Display Pathname': 'pwd', 'Remove Files': 'rm', 'Remove Directory':'rmdir', 'Rename Files': 'mv', 'Change Password': 'passwd', 'Display Logged In User': 'who'}

def process(s):
        return(s, "")

spoken_text = "Change Directory"
spoken_cmd, arguments = process(spoken_text)
command = commandDict[spoken_cmd]

print(command, arguments)

        


        
