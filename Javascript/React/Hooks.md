# useReducer

기존에 컴포넌트에서 useState를 이용하여 내부 state를 업데이트 하였는데, 이는 컴포넌트에 종속되는 문제가 있음. 이를 해결하기 위해 **컴포넌트와 state 업데이트 로직을 분리**하기 위해 사용.

- (useReducer vs Redux](https://recoderr.tistory.com/50)


# useMemo

성능 최적화를 위하여 **연산된 값을 재사용**하는 데 사용 됨. 반복해서 사용되는 컴포넌트를 memoization하여 rerendering을 줄이는 React.memo()와는 다름. 

# useCallback

useMemo 기반으로 만들어졌으며 **특정 함수를 새로만들지 않고 재사용하고싶을 때** 사용함. 기본적으로 함수는 컴포넌트가 리렌더링 될 때 마다 새로 만들어짐. 우리가 나중에 컴포넌트에서 props 가 바뀌지 않았으면 Virtual DOM 에 새로 렌더링하는 것 조차 하지 않고 컴포넌트의 결과물을 재사용 하는 최적화 작업을 할건데, 이 작업을 할 때 useCallback을 이용하는 것이 필요함.
