def solution(name, yearning, photo):
    if len(name) != len(yearning):
        raise Exception("name과 yearning의 개수가 일치하지 않음")
    
    # dict 생성
    name_yearning = {}
    for i in range(len(name)):
        name_yearning[name[i]] = yearning[i]
    # dict 값
    for person in name_yearning:
        print(f'{person}: {name_yearning[person]}')
        
    results = []
    
    for row in photo:
        result = 0 
        print("row : ", row)
        for x in row:
            if x in name_yearning.keys():
                result += name_yearning[x]
                print("result : ", result)
        results.append(result)

    print("results : ", results)
        
    return results

