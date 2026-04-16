# ============================================================================
# 6. 모드 1: 사용자 입력 (3×3)
# ============================================================================

def mode_user_input():
    """모드 1: 사용자가 직접 입력하는 3×3 필터/패턴 분석"""
    print("\n" + "=" * 50)
    print("# [모드 1] 사용자 입력 (3×3)")
    print("=" * 50)
    
    # 필터 A, B 입력
    print("\n#---------------------------------------")
    print("# [1] 필터 입력")
    print("#---------------------------------------")
    
    filter_a = read_matrix_from_console("필터 A (3줄 입력, 공백 구분):", 3)
    if not filter_a:
        return
    
    filter_b = read_matrix_from_console("필터 B (3줄 입력, 공백 구분):", 3)
    if not filter_b:
        return
    
    # 패턴 입력
    print("\n#---------------------------------------")
    print("# [2] 패턴 입력")
    print("#---------------------------------------")
    
    pattern = read_matrix_from_console("패턴 (3줄 입력, 공백 구분):", 3)
    if not pattern:
        return
    
    # MAC 연산
    print("\n#---------------------------------------")
    print("# [3] MAC 결과")
    print("#---------------------------------------")
    
    try:
        score_a = compute_mac(filter_a, pattern)
        score_b = compute_mac(filter_b, pattern)
        avg_time = measure_mac_time(filter_a, pattern, iterations=10)
        
        print(f"A 점수: {score_a}")
        print(f"B 점수: {score_b}")
        print(f"연산 시간(평균/10회): {avg_time:.6f} ms")
        
        result = judge_scores(score_a, score_b)
        if result == 'UNDECIDED':
            print(f"판정: 판정 불가 (|A-B| = {abs(score_a - score_b):.2e} < {EPSILON})")
        else:
            print(f"판정: {result}")
    
    except Exception as e:
        print(f"오류: {e}")