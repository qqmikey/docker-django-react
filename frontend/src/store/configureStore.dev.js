import { applyMiddleware, compose, createStore } from 'redux';
import thunk from 'redux-thunk';

import createRootReducer from '../rootReducer';


const history = null;

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const enhancer = composeEnhancers(applyMiddleware(thunk));

function configureStore(initialState) {
  return createStore(createRootReducer(history), initialState, enhancer);
}

export default {
  configureStore,
  history
};
