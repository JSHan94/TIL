# Reference

Move 관련 세미나 [유튜브 자료](https://www.youtube.com/watch?v=EG2-7bQNPv4) 요약

# Introduction

### What is Blockchain?

- 기존 CS에서 블록체인과 가장 유사한 개념은 Replicated state machine
- Replicas ("validators") agree on State 0 ("genesis"), tx order ("consensus), and function f(State, Transaction) &rarr; State
- 블록체인에 적합한 언어는 어떠해야하는가
    - Transaction = 프로그램임 (function + args)
    - Smart Contract = Tx에 의해 호출된 state 내부에 있는 Code
    - Move는 블록체인을 개발하기 위해 사용되는 language가 아닌, Blockchain language임 (Tx를 실행시키기 위한 Language는 어떻게해야하는가? 등의 Language semantics에 집중)
    - Blockchain Language가 가져야하는 필수 속성
        - Deterministic
            - state machine replication의 요구사항
        - Type and memory-safe
            - attacker에 의해 코드가 직접적으로 호출 될 수 있는 상황 등 가정
        - Metered execution (i.e. "gas")
            - 트랜잭션이 무한정 동작하여 전체 시스템이 멈추는 문제 해결
        - 기존 language들은 이런 속성을 가지지 못했음
- 스마트 컨트랙트의 보안적 이슈 해결방법
    - Subtract
        - re-entrancy, integer overflow등 버그 제거
    - Isolate
        - untrusted code와의 interaction 제한
    - Be careful
        - Audit, test, verify ...
    - 하지만 이들은 근본적 해결책은 아님 (병이 아닌 증상을 치료하는 것과 같음)
    - real-world의 자산을 encoding하고 transferring할 좋은 디자인 abstraction이나 untrusted code와 직접적으로 interact하는 안전한 코드를 작성하는 것은 어려움
- Desirable properties of blockchain lang
    - custom asset을 지원하는 언어
    - contract간 코드나 타입이 재사용 가능한 언어
    - platform간 코드 재사용이 가능한 언어

# How move does better?
- Resource safety guarantee (Digital money를)
    - Duplication
    - Double spending
    - Destruction


# A safety theorem for programming with money
 
