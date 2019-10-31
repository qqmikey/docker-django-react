import { applyMiddleware, createStore } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension/logOnlyInProduction';

import createRootReducer from '../rootReducer';


const history = null;
const enhancer = composeWithDevTools({})(applyMiddleware(thunk));


function configureStore(initialState) {
  return createStore(createRootReducer(history), initialState, enhancer);
}

export default {
  configureStore,
  history
};
