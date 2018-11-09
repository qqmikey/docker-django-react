import { createStore, compose, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
// eslint-disable-next-line import/no-extraneous-dependencies
import { createBrowserHistory } from 'history';
import { routerMiddleware } from 'connected-react-router';

import createRootReducer from '../rootReducer';
// import type { counterStateType } from '../reducers/types';


// const history = createHashHistory();
const history = createBrowserHistory();
const router = routerMiddleware(history);
const enhancer = compose(applyMiddleware(thunk, router));

// function configureStore(initialState?: counterStateType) {
//     return createStore(rootReducer, initialState, enhancer);
// }

function configureStore(initialState) {
  return createStore(createRootReducer(history), initialState, enhancer);
}

export default {
  configureStore,
  history
};
