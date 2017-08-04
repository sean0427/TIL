import { combinReducers, createStore } from 'redux'
import broadApp from '../src/reducers/index'
import { readBroad } from '../src/actions/index'
let store = createStore(broadApp);

store.dispatch(readBroad({a: 'b'}))
console.log(store.getState())

store.dispatch(readBroad({a: 'c'}))
console.log(store.getState())
