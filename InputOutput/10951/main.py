while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break
    '''try except:
        예외처리를 위한 구문
        except에 오류에 대한 구문이 들어간다.
        입력 도중에 파일의 끝을 만나면 EOFError가 발생합니다. (EOF: 파일의 끝(End of File))
    
    map: map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니다
    ''' 