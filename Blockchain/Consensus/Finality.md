# Finality

<p>
  블록체인에서 Finality란 트랜잭션이 블록에 포함되고, 되돌릴 수 없는 상태를 의미함. 크게 확률적 finality와 절대적 finality가 존재함<br/>
  비트코인에서 네트워크 딜레이 등으로 각 노드가 가지고 있는 체인이 다를 수가 있는데, 이런 상태는 finality가 보장되지 않은 것 임.<br/>
  실제 서로 다른 블록체인을 갖고 있는 노드가 만날 경우 서로 경쟁하게 됨.<br/>
</p>

<details>
<summary>확률적 Finality</summary>
<p>
  블록을 되돌릴 수 없다는 것이 확률적으로만 보장 됨. 비트코인의 경우가 해당됨.<br/>
  해시파워가 25%인 악의적 공격자가 비트코인을 공격할 경우 6개의 블록의 컨펌이 있다면, 해당 트랜잭션은 99% 이상의 확률로 배제되어 질 수 있음.<br/>
</p>
</details>

<details>
<summary>절대적 Finality</summary>
<p>
  한번 블록이 결정 되면 어떤 경우에도 되돌릴 수 없는 형태. 텐더민트 같은 BFT 계열의 합의 알고리즘이 해당됨.<br/>
  voting power의 2/3 prevote와 2/3의 pre commit을 받으면 해당 블록은 finalize 됨.<br/>
  하지만 BFT 기반의 합의 알고리즘을 쓸 경우 매번 새로운 validator가 추가 될 때마다 모든 validator가 서로를 확인해야하는 과정에서의 비용이 큼.<br/>
</p>
</details>
