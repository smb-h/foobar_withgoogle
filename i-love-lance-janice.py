# python 2.7.13

def solution(string):
    new_string = ""
    a_z = "abcdefghijklmnopqrstuvwxyz"
    z_a = "zyxwvutsrqponmlkjihgfedcba"
    for char in string:
        # check if its lowercase a to z character
        if char in a_z:
            new_string += z_a[a_z.index(char)]
        else:
            new_string += char
    return new_string

print solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
print solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
print solution(""vmxibkgrlm"")
