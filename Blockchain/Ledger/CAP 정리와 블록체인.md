# CAP 정리

Eric Brewer가 1998에 낸 가설로, 2002년에 정리로 입증 됨<br/>
어떤 분산 시스템이든 Consistency, Availability, Partition Tolerance를 동시에 모두 제공하지 못한 다는 정리<br/>

<img src="https://cryptographics.info/wp-content/uploads/2018/05/resized/1920/736/65/0/0/0/0/CAP-Theorem-The-Parts.png"/>

- Consistency : 분산 시스템의 모든 노드가 단 하나의, 동일한, 최신 데이터 사본을 갖도록 함
- Availability : 각 노드에서 데이터가 사용 가능하고 노드들이 요청에 응답 함
- Partition Tolerance : 네트워크 장애로 인해 노드 그룹이 다른 노드와 통신할 수 없는 경우에도 분산 시스템이 올바르게 동작 함

# 블록체인에서의 CAP

참여노드가 전세계에 분산된 블록체인의 경우 Partition Tolerance를 가지므로 Consitency와 Availability 중 하나만 충족 시키는 것이 가능함<br/>
일반적으로 노드가 겪게되는 두가지 유형의 결함이 있음
- Fail-stop fault : 노드가 고장난 경우 발생하는 장애 정지 결함
- Byzantine Fault : 노드가 악이적이거나 임의로 consistency에 어긋난 동작을 하는 경우. PBFT가 이를 해결하는 데 적합함.

확률적 Finality를 채택한 경우에는 Availability를 보장함. 네트워크 파티션에서 각 파티션에 포크가 생기고, 네트워크 파티션이 사라지면 longest-chain 규칙에 따라 다시 하나로 합쳐지게 됨<br/>
포크난 상황에서도 계속 합의가 가능하지만 Finality(Consistency)는 보장하지 못함<br/>
이와 달리 절대적 Finality를 선택할 경우 파티션 상황에서 Consistency를 보장함. 네트워크가 반으로 파티션되면 어느 한쪽도 2/3의 투표를 얻지 못해 합의가 불가능함
파티션이 사라지면 다시 합의 가능. 파티션 상황에서 Availability를 보장하지 못하는 대신 절대적 Finality를 보장할 수 있음<br/>



[Finality](https://github.com/JSHan94/TIL/blob/main/Blockchain/Ledger/Finality.md)

