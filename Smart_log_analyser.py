def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(txt, pattern):
    lps = build_lps(pattern)
    
    i = 0
    j = 0
    
    while i < len(txt):
        if pattern[j] == txt[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return True
        
        elif i < len(txt) and pattern[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return False

def analyser_ctrl(file_path):
    error_count = 0
    info_count = 0
    warning_count = 0
    errors = []
    
    with open(file_path, 'r') as file:
        for line in file:
            # we can simply use the inbuild function "in" but I want to show the KMP algorithm.
            # Doing this just because I can lol.
            # Also, its fun to implement something you learned in class :D
            if kmp_search (line, "ERROR"):
                error_count += 1
                errors.append(line.strip())
            elif kmp_search (line, "INFO"):
                info_count += 1
            elif kmp_search (line, "WARNING"):
                warning_count += 1
            else:
                continue
            
    print("\nLog Analysis Report")
    print("-------------------")

    print("Errors:", error_count)
    print("Warnings:", warning_count)
    print("Info:", info_count)

    common_errors = sorted({e: errors.count(e) for e in set(errors)}.items(), key=lambda x: x[1], reverse=True)[:5]

    print("\nTop Errors")

    for err, count in common_errors:
        print(f"{count}x - {err}")
        
    return

if __name__ == "__main__":
    path = input("Enter the log's path: ")
    analyser_ctrl(path)